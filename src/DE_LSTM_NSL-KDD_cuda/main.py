from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch
import numpy as np
import sys
import preprocess
from Mutation import mutation
from Crossover import crossover
from Selection import selection
import random as rand
import time

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
trainData = "train.txt"
testData = "test.txt"
hiddenLayer = 1
outputLayer = 5
batchSize = 10000
iteration = 40
epoch = 80
population = 20
F = 0.5
CR = 0.3

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
# bestAccuracy = 0
# bestPrecision = 0
# bestRecall = 0
bestSolution = np.zeros(int(hiddenLayer)+1).astype(float)
eachIterationLocalBestMetrics = []
eachIterationLocalBestSolution = np.zeros((int(population), len(bestSolution)), dtype=np.float)
Ud = np.size(train_noStringTemp_X, 1)
Ld = int(outputLayer)

# learning rate
Lr_Ud = 0.01
Lr_Ld = 0.001

# Initial
populationDataOriginal = np.zeros((int(population), len(bestSolution)), dtype=np.float)
for eachpopulationData_colum in range(int(population)):
    for eachpopulationData_row in range(np.size(populationDataOriginal, 1)):
        r = rand.random()
        if eachpopulationData_row == 0:
            # initial neurons
            populationDataOriginal[eachpopulationData_colum][eachpopulationData_row] = int(((Ud - Ld) * r) + Ld)
        elif eachpopulationData_row == 1:
            # intial learning rate
            r = r / 100 # learning rate [0.01 ~ 0.001]
            populationDataOriginal[eachpopulationData_colum][eachpopulationData_row] = float(((Lr_Ud - Lr_Ld) * r) + Lr_Ld)
populationData = populationDataOriginal.copy() # copy populationDataOriginal to populationData

for eachiteration in range(int(iteration)):
    if eachiteration != 0:
        print(best)
        print(bestSolution)

    # Mutation
    mutationData = mutation(populationData, float(F), Ud, Ld, Lr_Ud, Lr_Ld)
    
    # Crossover
    crossoverData = crossover(populationDataOriginal, mutationData, float(CR), Ud, Ld, Lr_Ud, Lr_Ld)
    
    # Selection
    countOriginalOtherAccuracy = np.zeros((4, int(population)))
    countCrossoverOtherAccuracy = np.zeros((4, int(population)))
    crossoverModel = []
    originalModel = []
    selectionData = selection(crossoverModel, originalModel, populationDataOriginal, crossoverData, countOriginalOtherAccuracy, countCrossoverOtherAccuracy, int(hiddenLayer), int(outputLayer), int(epoch), int(batchSize), train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
    
    # Fitness
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
            for j in range(2):
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
            for j in range(2):
                bestSolution[j] = selectionData[i][j]
    
    # Update
    eachIterationLocalBestMetrics.append(best) # save each iteration best local metrics
    
    # save each iteration best local solution
    for dim in range(np.size(eachIterationLocalBestSolution, 1)):
        eachIterationLocalBestSolution[eachiteration][dim] = bestSolution[dim] 
    
    if eachiteration >= 4:
        index = 0
        count = 0
        totalNeurons = 0
        totalLearningRate = 0

        for j in range(len(eachIterationLocalBestMetrics)):
            if eachIterationLocalBestMetrics[index] != eachIterationLocalBestMetrics[j]:
                count = 0
                index = j
                count += 1
            else:
                count +=1
        
        # if five iteration same
        if count >= 5:
            for i in range(count):
                # calculate neurons avg
                totalNeurons += eachIterationLocalBestSolution[i][0]
                
                # calculate learning rate avg
                totalLearningRate += eachIterationLocalBestSolution[i][1]
            totalNeurons /= (eachiteration + 1)
            totalLearningRate /= (eachiteration + 1)

            # reset
            ran = rand.randint(0, int(population)-1)
            populationDataOriginal = selectionData.copy()
            populationData = selectionData.copy()
            
            for dim in range(2):
                # neurons
                if dim == 0:
                    populationDataOriginal[ran][dim] = int(totalNeurons)
                    populationData[ran][dim] = int(totalNeurons)
                # learning rate
                elif dim == 1:
                    populationDataOriginal[ran][dim] = totalLearningRate
                    populationData[ran][dim] = totalLearningRate
    else:    
        # reset
        populationDataOriginal = selectionData.copy()
        populationData = selectionData.copy()

print(best)
print(bestSolution)
# print(bestAccuracy)
# print(bestPrecision)
# print(bestRecall)
torch.save(bestModel, 'DE_lstm.pkl')