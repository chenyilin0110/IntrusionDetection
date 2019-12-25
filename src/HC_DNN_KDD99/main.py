from torch.autograd import Variable
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
import random as rand
from neuralnetwork import Net
import preprocess
import accuracyfunction
from transaction import transaction
import time

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing iteration
trainData = sys.argv[1]
testData = sys.argv[2]
hiddenLayer = sys.argv[3]
outputLayer = sys.argv[4]
iteration = sys.argv[5]
epoch = sys.argv[6]

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

solution = np.zeros(int(hiddenLayer))
solution = solution.astype(int)
for i in range(len(solution)):
    solution[i] = rand.randint(int(outputLayer), int(np.size(train_resultNormalize, 1)))
# best = np.zeros(4, dtype=float)
best = 0

for eachiteration in range(int(iteration)):
    # build network
    net = Net(np.size(train_resultNormalize, 1), int(outputLayer), int(hiddenLayer), solution)
    
    # set optimizer and loss_function
    optimizer = optim.Adam(net.parameters(), lr = 0.01)
    lossFunction = nn.CrossEntropyLoss()

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
    pred = y_test_predic.detach().numpy()
    y_test_list_predic = np.argmax(pred, axis=1)

    # print(filename, " ", end='')
    accuracy = accuracyfunction.accuracy(y_test_tensor, y_test_list_predic)    

    # compare f1score
    if best <= accuracy:        
        best = accuracy
        bestSolution = solution.copy()
    else:
        for i in range(np.size(bestSolution)):
            solution[i] = bestSolution[i]
    
    if eachiteration != int(iteration)-1:
        # transaction
        solution = transaction(solution, np.size(train_resultNormalize, 1), int(hiddenLayer), int(outputLayer))
    print(best)