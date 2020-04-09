from fitness import fitness
import numpy as np

def selection(crossoverModel, originalModel, populationDataOriginal, crossoverData, countOriginalLossValue, countCrossoverLossValue, hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, train_loader, cuda):
    selectionPopulationData = populationDataOriginal
    
    for eachPopulation in range(np.size(populationDataOriginal,0)):
        countOriginalLossValue[0][eachPopulation],  model = fitness(populationDataOriginal[eachPopulation], hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, train_loader, cuda)
        originalModel.append(model)

        countCrossoverLossValue[0][eachPopulation], model = fitness(crossoverData[eachPopulation], hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, train_loader, cuda)
        crossoverModel.append(model)

    for eachPopulation in range(np.size(countCrossoverLossValue, 1)):
        if countCrossoverLossValue[0][eachPopulation] <= countOriginalLossValue[0][eachPopulation]:
            for eachDim in range(hiddenLayer):
                selectionPopulationData[eachPopulation][eachDim] = crossoverData[eachPopulation][eachDim]
    return selectionPopulationData