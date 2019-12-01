from sklearn.model_selection import train_test_split
from torch.autograd import Variable
import torch
import numpy as np
import sys
import random as rand
import preprocess
from mutation import mutation
from crossover import crossover
from selection import selection
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
hiddenLayer = sys.argv[4]
hiddenNeural = sys.argv[5]
testing = sys.argv[6]
iteration = sys.argv[7]
epoch = sys.argv[8]
population = sys.argv[9]
F = sys.argv[10]
CR = sys.argv[11]

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

# split data
x_train, x_test, y_train, y_test = train_test_split(resultNormalize, noStringTemp_Y, test_size = float(testing)/100)

# np->tensor
x_train_tensor = Variable(torch.from_numpy(x_train)).float()
y_train_tensor = Variable(torch.from_numpy(y_train)).long()
x_test_tensor = Variable(torch.from_numpy(x_test)).float()
y_test_tensor = Variable(torch.from_numpy(y_test)).long()

best = 0
bestAccuracy = 0
bestPrecision = 0
bestRecall = 0
bestSolution = np.zeros(int(hiddenLayer)).astype(int)
Ud = np.size(noStringTemp_X, 1)
Ld = int(outputLayer)

# Initial
populationDataOriginal = np.zeros((int(population), len(bestSolution)), dtype=np.int)
for eachpopulationData_colum in range(int(population)):
    for eachpopulationData_row in range(np.size(populationDataOriginal, 1)):
        r = rand.random()
        populationDataOriginal[eachpopulationData_colum][eachpopulationData_row] = int(((Ud - Ld) * r) + Ld)
populationData = populationDataOriginal.copy() # copy populationDataOriginal to populationData

for eachiteration in range(int(iteration)):
    # Mutation
    mutationData = mutation(populationData, float(F), Ud, Ld)
    
    # Crossover
    crossoverData = crossover(populationDataOriginal, mutationData, float(CR), Ud, Ld)
    
    # Selection
    # countOriginalFitness = []
    # countCrossoverFitness = []
    countOriginalOtherAccuracy = np.zeros((4, int(population)))
    countCrossoverOtherAccuracy = np.zeros((4, int(population)))
    selectionData = selection(populationDataOriginal, crossoverData, countOriginalOtherAccuracy, countCrossoverOtherAccuracy, int(hiddenLayer), int(outputLayer), int(epoch), noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
    
    if eachiteration == 0:
        best = countCrossoverOtherAccuracy[1][0]

    for i in range(np.size(countCrossoverOtherAccuracy, 1)):
        if best <= countCrossoverOtherAccuracy[1][i]:
            best = countCrossoverOtherAccuracy[1][i]
            bestAccuracy = countCrossoverOtherAccuracy[0][i]
            bestPrecision = countCrossoverOtherAccuracy[2][i]
            bestRecall = countCrossoverOtherAccuracy[3][i]
            for j in range(int(hiddenLayer)):
                bestSolution[j] = selectionData[i][j]
            

    for i in range(np.size(countCrossoverOtherAccuracy, 1)):
        if best <= countOriginalOtherAccuracy[1][i]:
            best = countOriginalOtherAccuracy[1][i]
            bestAccuracy = countOriginalOtherAccuracy[0][i]
            bestPrecision = countOriginalOtherAccuracy[2][i]
            bestRecall = countOriginalOtherAccuracy[3][i]
            for j in range(int(hiddenLayer)):
                bestSolution[j] = selectionData[i][j]

    # reset
    populationDataOriginal = selectionData.copy()
    populationData = selectionData.copy()
print(bestAccuracy)
print(best)
print(bestSolution)
print(bestPrecision)
print(bestRecall)
# print(best,"",end='')
# print(bestSolution)
    # training 
    # y_train_predict = net(x_train_tensor, int(hiddenLayer))
    # pred = y_train_predict.detach().numpy()
    # y_train_list_predic = np.argmax(pred, axis=1)
    # print("The training accuracy is", accuracyfunction.accuracy(y_train_tensor, y_train_list_predic))
    # print()