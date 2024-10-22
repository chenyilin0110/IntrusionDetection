from sklearn.model_selection import train_test_split
from torch.autograd import Variable
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
from neuralnetwork import Net
import preprocess
import accuracyfunction
#import matplotlib.pyplot as plt
#import seaborn as sns

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing epoch
finder = sys.argv[1]
filename = sys.argv[2]
outputLayer = sys.argv[3]
hiddenLayer = sys.argv[4]
hiddenNeural = sys.argv[5]
testing = sys.argv[6]
epoch = sys.argv[7]

# load dataset
if finder == "multi":
    temp = np.loadtxt('dataSet/IndustrialControlSystem/multiclass/'+filename, dtype=np.str, delimiter=',')
elif int(finder) == 2:
    temp = np.loadtxt('dataSet/IndustrialControlSystem/2class/'+filename, dtype=np.str, delimiter=',')
elif int(finder) == 3:
    temp = np.loadtxt('dataSet/IndustrialControlSystem/3class/'+filename, dtype=np.str, delimiter=',')

if finder =="multi":
    noStringTemp = temp[0:,0:] 
else:
    noStringTemp = temp[1:,0:] #[欄,列] and clean top string

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

# build network
net = Net(np.size(noStringTemp_X,1), int(outputLayer), int(hiddenLayer), int(hiddenNeural))

# set optimizer and loss_function
optimizer = optim.Adam(net.parameters(), lr = 0.01)
lossFunction = nn.CrossEntropyLoss()

# split data
x_train, x_test, y_train, y_test = train_test_split(resultNormalize, noStringTemp_Y, test_size = float(testing)/100)

# np->tensor
x_train_tensor = Variable(torch.from_numpy(x_train)).float()
y_train_tensor = Variable(torch.from_numpy(y_train)).long()
x_test_tensor = Variable(torch.from_numpy(x_test)).float()
y_test_tensor = Variable(torch.from_numpy(y_test)).long()

# calculate parameters
for eachepoch in range(1,int(epoch)+1):
    y_train_predict = net(x_train_tensor, int(hiddenLayer))# cell net.forward() and return predict    
    loss_train = lossFunction(y_train_predict, y_train_tensor)# calculate loss
#    if epoch % 100 ==0:
#        print('epoch',loss_train.item())    
    optimizer.zero_grad()# clean optimizer
    loss_train.backward()# calculate new parameters
    optimizer.step()# update parameters

# testing 
y_test_predic = net(x_test_tensor, int(hiddenLayer))
pred = y_test_predic.detach().numpy()#training's cannot impact testing
y_test_list_predic = np.argmax(pred, axis=1)

accuracyfunction.accuracy(y_test_tensor, y_test_list_predic)