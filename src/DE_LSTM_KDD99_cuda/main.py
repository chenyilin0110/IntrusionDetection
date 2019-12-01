from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch
import numpy as np
import sys
import preprocess
from mutation import mutation
from crossover import crossover
from selection import selection
import random as rand
import time

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing iteration
# trainData = sys.argv[1]
# testData = sys.argv[2]
# testData_21 = sys.argv[3]
# hiddenLayer = sys.argv[4]
# outputLayer = sys.argv[5]
# batchSize = sys.argv[6]
# iteration = sys.argv[7]
# epoch = sys.argv[8]
# population = sys.argv[9]
# F = sys.argv[10]
# CR = sys.argv[11]
trainData = "train"
testData = "test"
hiddenLayer = 1
outputLayer = 5
batchSize = 100
iteration = 1
epoch = 80
population = 3
F = 0.5
CR = 0.3

# can use cuda or not
cuda = torch.cuda.is_available()

# load dataset
train_noStringTemp_X = preprocess.loadDataset(trainData)
test_noStringTemp_X = preprocess.loadDataset(testData)

train_temp = preprocess.originalDataset(trainData)
test_temp = preprocess.originalDataset(testData)

train_noStringTemp_Y = []
train_noStringTemp_Y = preprocess.distinguishNaturalAttack(train_temp, train_noStringTemp_Y, int(outputLayer))
test_noStringTemp_Y = []
test_noStringTemp_Y = preprocess.distinguishNaturalAttack(test_temp, test_noStringTemp_Y, int(outputLayer))

# start preprocess----------------------------------------------------------------------------------------------------------

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
bestAccuracy = 0
bestPrecision = 0
bestRecall = 0
bestSolution = np.zeros(int(hiddenLayer)).astype(int)
eachIterationLocalBest = []
Ud = np.size(train_noStringTemp_X, 1)
Ld = int(outputLayer)

# Initial
populationDataOriginal = np.zeros((int(population), len(bestSolution)), dtype=np.int)
for eachpopulationData_colum in range(int(population)):
    for eachpopulationData_row in range(np.size(populationDataOriginal, 1)):
        r = rand.random()
        populationDataOriginal[eachpopulationData_colum][eachpopulationData_row] = int(((Ud - Ld) * r) + Ld)
populationData = populationDataOriginal.copy() # copy populationDataOriginal to populationData

for eachiteration in range(int(iteration)):
    if eachiteration != 0:
        print(best)
        print(bestSolution)
    # Mutation
    mutationData = mutation(populationData, float(F), Ud, Ld)
    
    # Crossover
    crossoverData = crossover(populationDataOriginal, mutationData, float(CR), Ud, Ld)
    
    # Selection
    countOriginalOtherAccuracy = np.zeros((4, int(population)))
    countCrossoverOtherAccuracy = np.zeros((4, int(population)))
    crossoverModel = []
    originalModel = []
    selectionData = selection(crossoverModel, originalModel, populationDataOriginal, crossoverData, countOriginalOtherAccuracy, countCrossoverOtherAccuracy, int(hiddenLayer), int(outputLayer), int(epoch), int(batchSize), train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor, cuda)
    
    if eachiteration == 0:
        # best = countCrossoverOtherAccuracy[1][0]
        best = countCrossoverOtherAccuracy[0][0]
        bestModel = crossoverModel[0]

    for i in range(np.size(countCrossoverOtherAccuracy, 1)):
        # if best <= countCrossoverOtherAccuracy[1][i]:
            # best = countCrossoverOtherAccuracy[1][i]
        if best <= countCrossoverOtherAccuracy[0][i]:
            best = countCrossoverOtherAccuracy[0][i]
            bestModel = crossoverModel[i]
            # bestAccuracy = countCrossoverOtherAccuracy[0][i]
            # bestPrecision = countCrossoverOtherAccuracy[2][i]
            # bestRecall = countCrossoverOtherAccuracy[3][i]
            for j in range(int(hiddenLayer)):
                bestSolution[j] = selectionData[i][j]

    for i in range(np.size(countCrossoverOtherAccuracy, 1)):
        # if best <= countOriginalOtherAccuracy[1][i]:
        #     best = countOriginalOtherAccuracy[1][i]
        if best <= countOriginalOtherAccuracy[0][i]:
            best = countOriginalOtherAccuracy[0][i]
            bestModel = originalModel[i]
            # bestAccuracy = countOriginalOtherAccuracy[0][i]
            # bestPrecision = countOriginalOtherAccuracy[2][i]
            # bestRecall = countOriginalOtherAccuracy[3][i]
            for j in range(int(hiddenLayer)):
                bestSolution[j] = selectionData[i][j]
    
    eachIterationLocalBest.append(bestSolution[0]) # save each iteration best local
    index = 0
    count = 0
    total = 0
    if eachiteration >= 4:
        for j in range(len(eachIterationLocalBest)):
            if eachIterationLocalBest[index] != eachIterationLocalBest[j]:
                count = 0
                index = j
                count += 1
            else:
                count +=1
        
        if count >= 5: # five iteration same
            for i in range(len(eachIterationLocalBest)):
                total += eachIterationLocalBest[i]
            total /= (eachiteration + 1)

            # reset
            ran = rand.randint(0, int(population)-1)
            populationDataOriginal = selectionData.copy()
            populationData = selectionData.copy()
            populationDataOriginal[ran] = int(total)
            populationData[ran] = int(total)
    else:    
        # reset
        populationDataOriginal = selectionData.copy()
        populationData = selectionData.copy()
# print(bestAccuracy)
print(best)
print(bestSolution)
# print(bestPrecision)
# print(bestRecall)
torch.save(bestModel, 'src/DE_LSTM_KDD99_cuda/result/DE_lstm.pkl')