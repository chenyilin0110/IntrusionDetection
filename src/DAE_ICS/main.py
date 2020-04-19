from sklearn.model_selection import train_test_split
from torch.autograd import Variable
import torch
import torch.optim as optim
import torch.nn as nn
import numpy as np
import sys
import random as rand
import preprocess
from neuralnetwork import DeepAutoEncoder
from accuracyfunction import accuracy
import time
#import matplotlib.pyplot as plt
#import seaborn as sns

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing iteration
finder = sys.argv[1]
filename = sys.argv[2]
outputLayer = sys.argv[3]
test = sys.argv[4]
epoch = sys.argv[5]
number = sys.argv[6]

# can use cuda or not
cuda = torch.cuda.is_available()

# load dataset
noStringTemp = preprocess.load(finder, filename)
noStringTemp_X = noStringTemp[0:,0:-1]

# preprocess
noStringTemp_X = preprocess.missingValue(noStringTemp_X)
if finder != "multi":
    noStringTemp_Y = []
    noStringTemp_Y = preprocess.distinguishNaturalAttack(noStringTemp, noStringTemp_Y)
    # list->np
    noStringTemp_Y = np.array(noStringTemp_Y)    
else:
    noStringTemp_Y = noStringTemp[:,-1]    
    noStringTemp_Y = noStringTemp_Y.astype(int)
    # multiclass 1 to 41, but lossfunction from 0 begin
    for i in range(len(noStringTemp_Y)):
        noStringTemp_Y[i] -= 1

resultNormalize = preprocess.normalize(noStringTemp_X)

# np->tensor but noStringTemp_X is not float so astype(x)
noStringTemp_X = noStringTemp_X.astype(float)

# split data
x_train, x_test, y_train, y_test = train_test_split(resultNormalize, noStringTemp_Y, test_size = float(test)/100)

# np->tensor
x_train_tensor = Variable(torch.from_numpy(x_train)).float()
y_train_tensor = Variable(torch.from_numpy(y_train)).long()
x_test_tensor = Variable(torch.from_numpy(x_test)).float()
y_test_tensor = Variable(torch.from_numpy(y_test)).long()

# end preprocess----------------------------------------------------------------------------------------------------------

# bulid DeepAutoEncoder
DAE = DeepAutoEncoder(np.size(noStringTemp_X,1), int(outputLayer))

# set optimizer and lossFunction
optimizer = optim.Adam(DAE.parameters(), lr=0.05)
lossFunction = nn.CrossEntropyLoss()

if cuda == True:
    DAE.cuda()

# traning
for eachepoch in range(int(epoch)):
    batch_x = x_train_tensor.view(1, -1, np.size(noStringTemp_X, 1)) # seq_len batch_size input_dim
    
    if cuda == True:
        y_prediction = DAE(batch_x.cuda())
    else:
        y_prediction = DAE(batch_x)

    y_prediction = y_prediction.view(np.size(batch_x.numpy(), 1), -1) # reshape from 3 dimention to 2 dimention

    if cuda == True:
        loss = lossFunction(y_prediction, y_train_tensor.cuda())
    else:
        loss = lossFunction(y_prediction, y_train_tensor)
    # print(loss.item())
    optimizer.zero_grad()# clean optimizer
    loss.backward(retain_graph=True)# calculate new parameters
    optimizer.step()# update parameters

x_test = x_test_tensor.view(1, -1, np.size(noStringTemp_X, 1))

if cuda == True:
    y_test_predic = DAE(x_test.cuda())
else:
    y_test_predic = DAE(x_test)

pred = y_test_predic.detach().cpu().numpy()
pred = pred.reshape(-1, int(outputLayer))
y_test_list_predic = np.argmax(pred, axis=1)

accuracyvalue = accuracy(y_test_tensor, y_test_list_predic)
print(accuracyvalue)
torch.save(DAE, 'src/DAE_ICS/result/DAE' + outputLayer + '-' + number + '.pkl')