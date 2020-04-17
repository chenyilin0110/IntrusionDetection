from fitness import fitness
import numpy as np

def selection(populationDataOriginal, crossoverData, countOriginalLossValue, countCrossoverLossValue, crossoverModel, originalModel, hiddenLayer, outputLayer, epoch, noStringTemp_X, x_train_tensor, y_train_tensor):
    selectionPopulationData = populationDataOriginal
    
    for eachPopulation in range(np.size(populationDataOriginal,0)):
        countOriginalLossValue[0][eachPopulation], model = fitness(populationDataOriginal[eachPopulation], hiddenLayer, outputLayer, epoch, noStringTemp_X, x_train_tensor, y_train_tensor)
        originalModel.append(model)
        countCrossoverLossValue[0][eachPopulation], model = fitness(crossoverData[eachPopulation], hiddenLayer, outputLayer, epoch,  noStringTemp_X, x_train_tensor, y_train_tensor)
        crossoverModel.append(model)
        
    for eachPopulation in range(np.size(countCrossoverLossValue, 1)):
        if countCrossoverLossValue[0][eachPopulation] <= countOriginalLossValue[0][eachPopulation]:
            for eachDim in range(hiddenLayer):
                selectionPopulationData[eachPopulation][eachDim] = crossoverData[eachPopulation][eachDim]
    return selectionPopulationData