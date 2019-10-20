from sklearn.model_selection import train_test_split
from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
from neuralnetwork import AutoEncoder
import preprocess
from accuracyfunction import accuracy
import time

# set filename outputLayer testing iteration
trainData = sys.argv[1]
testData = sys.argv[2]
outputLayer = sys.argv[3]
epoch = sys.argv[4]

# can use cuda or not
cuda = torch.cuda.is_available()

# load dataset
train_noStringTemp_X, train_noStringTemp_Y = preprocess.loadDataset(trainData)
test_noStringTemp_X, test_noStringTemp_Y = preprocess.loadDataset(testData)

# duration src_bytes
for i in range(len(train_noStringTemp_X)):
    train_noStringTemp_X[i][0] = preprocess.log(train_noStringTemp_X[i][0])
    train_noStringTemp_X[i][4] = preprocess.log(train_noStringTemp_X[i][4])
    train_noStringTemp_X[i][5] = preprocess.log(train_noStringTemp_X[i][5])

for i in range(len(test_noStringTemp_X)):
    test_noStringTemp_X[i][0] = preprocess.log(test_noStringTemp_X[i][0])
    test_noStringTemp_X[i][4] = preprocess.log(test_noStringTemp_X[i][4])
    test_noStringTemp_X[i][5] = preprocess.log(test_noStringTemp_X[i][5])

# normalize
train_resultNormalize = preprocess.normalize(train_noStringTemp_X)
test_resultNormalize = preprocess.normalize(test_noStringTemp_X)

# np->tensor
x_train_tensor = Variable(torch.from_numpy(train_resultNormalize)).float()
y_train_tensor = Variable(torch.from_numpy(train_noStringTemp_Y)).long()
x_test_tensor = Variable(torch.from_numpy(test_resultNormalize)).float()
y_test_tensor = Variable(torch.from_numpy(test_noStringTemp_Y)).long()

# end preprocess----------------------------------------------------------------------------------------------------------

# bulid autoencoder
autdoencoder = AutoEncoder(np.size(train_noStringTemp_X,1), int(outputLayer))

# set optimizer and lossFunction
optimizer = optim.Adam(autdoencoder.parameters(), lr=0.05)
lossFunction = nn.CrossEntropyLoss()

if cuda == True:
    autdoencoder.cuda()

# traning
for eachepoch in range(int(epoch)):
    batch_x = x_train_tensor.view(1, -1, np.size(train_noStringTemp_X, 1)) # seq_len batch_size input_dim
    
    if cuda == True:
        y_prediction = autdoencoder(batch_x.cuda())
    else:
        y_prediction = autdoencoder(batch_x)

    y_prediction = y_prediction.view(np.size(batch_x.numpy(), 1), -1) # reshape from 3 dimention to 2 dimention
    loss = lossFunction(y_prediction, y_train_tensor.cuda())
    if cuda == True:
        loss = lossFunction(y_prediction, y_train_tensor.cuda())
    else:
        loss = lossFunction(y_prediction, y_train_tensor)
    optimizer.zero_grad()# clean optimizer
    loss.backward(retain_graph=True)# calculate new parameters
    optimizer.step()# update parameters

x_test = x_test_tensor.view(1, -1, np.size(train_noStringTemp_X, 1))

if cuda == True:
    y_test_predic = autdoencoder(x_test.cuda())
else:
    y_test_predic = autdoencoder(x_test)

pred = y_test_predic.detach().cpu().numpy()
pred = pred.reshape(-1, int(outputLayer))
y_test_list_predic = np.argmax(pred, axis=1)

accuracyvalue = accuracy(y_test_tensor, y_test_list_predic)
print(accuracyvalue)
torch.save(autdoencoder, 'src/Deep_Auto_Encoder/result/autoencoder' + outputLayer + '.pkl')