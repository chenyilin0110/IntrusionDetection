from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
from neuralnetwork import LSTM
import preprocess
from accuracyfunction import accuracy
import time

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing iteration
trainData = sys.argv[1]
testData = sys.argv[2]
outputLayer = sys.argv[3]
batchSize = sys.argv[4]
epoch = sys.argv[5]

# load dataset
train_noStringTemp_X = preprocess.loadDataset(trainData)
test_noStringTemp_X = preprocess.loadDataset(testData)

train_temp = preprocess.originalDataset(trainData)
test_temp = preprocess.originalDataset(testData)

train_noStringTemp_Y = []
train_noStringTemp_Y = preprocess.distinguishNaturalAttack(train_temp, train_noStringTemp_Y, int(outputLayer))
test_noStringTemp_Y = []
test_noStringTemp_Y = preprocess.distinguishNaturalAttack(test_temp, test_noStringTemp_Y, int(outputLayer))

# list->np
train_noStringTemp_X = np.array(train_noStringTemp_X)
train_noStringTemp_Y = np.array(train_noStringTemp_Y)
test_noStringTemp_X = np.array(test_noStringTemp_X)
test_noStringTemp_Y = np.array(test_noStringTemp_Y)

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

# bulid lstm
lstm = LSTM(np.size(train_resultNormalize,1), int(outputLayer))

# set optimizer and lossFunction
optimizer = optim.RMSprop(lstm.parameters(), lr=0.05)
lossFunction = nn.CrossEntropyLoss()

# split batch
batch_train_dataset = torch.utils.data.TensorDataset(x_train_tensor, y_train_tensor)
train_loader = torch.utils.data.DataLoader(batch_train_dataset, batch_size=int(batchSize), shuffle=False)

# traning
for eachepoch in range(int(epoch)):
    for step, (batch_x, batch_y) in enumerate (train_loader):
        batch_x = batch_x.view(1, -1, np.size(train_resultNormalize, 1)) # seq_len batch_size input_dim
        y_prediction = lstm(batch_x)
        y_prediction = y_prediction.view(np.size(batch_x.numpy(), 1), -1) # reshape from 3 dimention to 2 dimention
        loss = lossFunction(y_prediction, batch_y)
        optimizer.zero_grad()# clean optimizer
        loss.backward(retain_graph=True)# calculate new parameters
        optimizer.step()# update parameters

# testing
x_test_tensor = x_test_tensor.view(1, -1, np.size(train_resultNormalize, 1))
y_test_predic = lstm(x_test_tensor)
pred = y_test_predic.detach().numpy()
pred = pred.reshape(-1, int(outputLayer))
y_test_list_predic = np.argmax(pred, axis=1)

accuracy = accuracy(y_test_tensor, y_test_list_predic)
print(accuracy)
torch.save(lstm, 'src/LSTM_KDD99/result/lstm' + outputLayer + '.pkl')