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
from update import update
from testingfunction import testing
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
test = sys.argv[6]
iteration = sys.argv[7]
epoch = sys.argv[8]
population = sys.argv[9]
F = sys.argv[10]
CR = sys.argv[11]
number = sys.argv[12]

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

best = 9999
bestModel = 0
bestSolution = np.zeros(int(hiddenLayer)).astype(int)
eachIterationLocalBest = []
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
    countOriginalLossValue = np.zeros((4, int(population)))
    countCrossoverLossValue = np.zeros((4, int(population)))
    crossoverModel = []
    originalModel = []
    selectionData = selection(populationDataOriginal, crossoverData, countOriginalLossValue, countCrossoverLossValue, crossoverModel, originalModel, int(hiddenLayer), int(outputLayer), int(epoch), noStringTemp_X, x_train_tensor, y_train_tensor)
    
    # Update
    best, bestModel = update(best, bestModel, eachiteration, bestSolution, eachIterationLocalBest, int(population), countCrossoverLossValue, countOriginalLossValue, crossoverModel, originalModel, selectionData)

    # Save model
    torch.save(bestModel, 'src/DE_DNN_ICS/result/DE_DNN_' + outputLayer + '-' + number + '.pkl')

testing(outputLayer, hiddenLayer, x_test_tensor, y_test_tensor, number)