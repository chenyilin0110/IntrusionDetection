from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch
import numpy as np
import sys
import preprocess
from mutation import mutation
from crossover import crossover
from selection import selection
from update import update
from testingfunction import testing
import random as rand
import time
import os

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing iteration
trainData = sys.argv[1]
testData = sys.argv[2]
hiddenLayer = sys.argv[3]
outputLayer = sys.argv[4]
batchSize = sys.argv[5]
iteration = sys.argv[6]
epoch = sys.argv[7]
population = sys.argv[8]
F = sys.argv[9]
CR = sys.argv[10]
name = sys.argv[11]
number = sys.argv[12]

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

best = 0
bestModel = 0
bestSolution = np.zeros(2).astype(float)
eachIterationLocalBest = np.zeros((int(iteration), len(bestSolution)+1), dtype=float)
Ud = np.size(train_noStringTemp_X, 1)
Ld = int(outputLayer)
lrUd = 0.01
lrLd = 0.001

# Initial
populationDataOriginal = np.zeros((int(population), len(bestSolution)), dtype=np.float)
for eachpopulationData_colum in range(int(population)):
    for eachpopulationData_row in range(np.size(populationDataOriginal, 1)):
        if eachpopulationData_row == 0: # initial first bit(neurons)
            r = rand.random()
            populationDataOriginal[eachpopulationData_colum][eachpopulationData_row] = int(((Ud - Ld) * r) + Ld)
        else:
            r = rand.random()
            populationDataOriginal[eachpopulationData_colum][eachpopulationData_row] = ((lrUd - lrLd) * r) + lrLd
populationData = populationDataOriginal.copy() # copy populationDataOriginal to populationData

for eachiteration in range(int(iteration)):
    # split batch
    batch_train_dataset = torch.utils.data.TensorDataset(x_train_tensor, y_train_tensor)
    train_loader = torch.utils.data.DataLoader(batch_train_dataset, batch_size=int(batchSize), shuffle=True, num_workers=8)

    # Mutation
    mutationData = mutation(populationData, float(F), Ud, Ld, lrUd, lrLd)
    
    # Crossover
    crossoverData = crossover(populationDataOriginal, mutationData, float(CR), Ud, Ld, lrUd, lrLd)
    
    # Selection
    countOriginalLossValue = np.zeros((4, int(population)))
    countCrossoverLossValue = np.zeros((4, int(population)))
    crossoverModel = []
    originalModel = []
    selectionData = selection(crossoverModel, originalModel, populationDataOriginal, crossoverData, countOriginalLossValue, countCrossoverLossValue, int(hiddenLayer), int(outputLayer), int(epoch), int(batchSize), train_noStringTemp_X, x_train_tensor, y_train_tensor, train_loader, cuda)
    
    # Update
    best, bestModel = update(best, bestModel, eachiteration, bestSolution, eachIterationLocalBest, int(population), countCrossoverLossValue, countOriginalLossValue, crossoverModel, originalModel, selectionData, name)

    if name == '0':
        torch.save(bestModel, 'src/DE_LSTM_two_parameters_NSL-KDD/result/DE_LSTM_' + outputLayer + '_bs' + batchSize + '-' + number + '.pkl')
    else:
        torch.save(bestModel, 'src/DE_LSTM_two_parameters_NSL-KDD/result/DE_LSTM_' + outputLayer + name + '_bs' + batchSize + '-' + number + '.pkl')

testing(outputLayer, train_noStringTemp_X, x_test_tensor, y_test_tensor, cuda, name, batchSize, number)