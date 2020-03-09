from fitness import fitness
import numpy as np

def selection(crossoverModel, originalModel, populationDataOriginal, crossoverData, countOriginalLossValue, countCrossoverLossValue, hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, train_loader, cuda):
    selectionPopulationData = populationDataOriginal
    
    for eachPopulation in range(np.size(populationDataOriginal,0)):
        countOriginalLossValue[eachPopulation],  model = fitness(populationDataOriginal[eachPopulation], hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, train_loader, cuda)
        originalModel.append(model)

        crossoverModel.append([])
        for each in range(np.size(crossoverData, 1)):
            countCrossoverLossValue[eachPopulation][each], model = fitness(crossoverData[eachPopulation][each], hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, train_loader, cuda)
            crossoverModel[eachPopulation].append(model)

    for eachPopulation in range(np.size(countCrossoverLossValue, 0)):
        for each in range(np.size(countCrossoverLossValue, 1)):
            if countCrossoverLossValue[eachPopulation][each] <= countOriginalLossValue[eachPopulation]:
                for eachDim in range(hiddenLayer):
                    selectionPopulationData[eachPopulation][eachDim] = crossoverData[eachPopulation][each][eachDim]
    return selectionPopulationData