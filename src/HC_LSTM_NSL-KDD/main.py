from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
import random as rand
from neuralnetwork import LSTM
import preprocess
import accuracyfunction
from fitness import fitness
from transaction import transaction
from testingfunction import testing
#import matplotlib.pyplot as plt
#import seaborn as sns
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
batchSize = sys.argv[6]
epoch = sys.argv[7]
name = sys.argv[8]

# can use cuda or not
cuda = torch.cuda.is_available()

# load trainData
train_temp = preprocess.loadDataset(trainData)
train_noStringTemp_X = train_temp[0:,0:-1]

# start preprocess----------------------------------------------------------------------------------------------------------

# only trainData do this
protocal_type_list = preprocess.saveProtocal_typeOrder(train_noStringTemp_X)
service_list = preprocess.saveServiceOrder(train_noStringTemp_X)
flag_list = preprocess.saveFlagOrder(train_noStringTemp_X)
protocal_type_onehotencoded = preprocess.onehotencoded(protocal_type_list)
service_list_onehotencoded = preprocess.onehotencoded(service_list)
flag_list_onehotencoded = preprocess.onehotencoded(flag_list)

# load testData
test_temp = preprocess.loadDataset(testData)
test_noStringTemp_X = test_temp[0:,0:-1]

train_noStringTemp_Y = []
train_noStringTemp_Y = preprocess.distinguishNaturalAttack(train_temp, train_noStringTemp_Y, int(outputLayer))
test_noStringTemp_Y = []
test_noStringTemp_Y = preprocess.distinguishNaturalAttack(test_temp, test_noStringTemp_Y, int(outputLayer))

# np can't dynamic add number so use list
train_noStringTemp_X = train_noStringTemp_X.tolist() 
test_noStringTemp_X = test_noStringTemp_X.tolist()

# replace text with onehotencoded number
preprocess.replace(train_noStringTemp_X, protocal_type_list, service_list, flag_list, protocal_type_onehotencoded, service_list_onehotencoded, flag_list_onehotencoded)
preprocess.replace(test_noStringTemp_X, protocal_type_list, service_list, flag_list, protocal_type_onehotencoded, service_list_onehotencoded, flag_list_onehotencoded)

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
best = 999999999

for eachiteration in range(int(iteration)):
    loss_value, model = fitness(solution, hiddenLayer, outputLayer, epoch, int(batchSize), train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor, cuda)

    # compare f1score
    if best >= loss_value:        
        best = loss_value
        bestModel = model
        bestSolution = solution.copy()
    else:
        for i in range(np.size(bestSolution)):
            solution[i] = bestSolution[i]
    
    if eachiteration != int(iteration)-1:
        # transaction
        solution = transaction(solution, np.size(train_resultNormalize, 1), int(hiddenLayer), int(outputLayer))
    # print(best)
if name == '0':
    torch.save(bestModel, 'src/HC_LSTM_NSL-KDD/result/HC_LSTM_' + outputLayer + '.pkl')
else:
    torch.save(bestModel, 'src/HC_LSTM_NSL-KDD/result/HC_LSTM_' + outputLayer + name +'.pkl')
testing(outputLayer, train_resultNormalize, x_test_tensor, y_test_tensor,cuda, name)