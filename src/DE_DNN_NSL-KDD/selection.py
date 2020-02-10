from fitness import fitness
import numpy as np

def selection(crossoverModel, originalModel, populationDataOriginal, crossoverData, countOriginalLossValue, countCrossoverLossValue, hiddenLayer, outputLayer, epoch, train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor):
    selectionPopulationData = populationDataOriginal
    
    for eachPopulation in range(np.size(populationDataOriginal,0)):
        # accuracy, local, precision, recall = fitness(populationDataOriginal[eachPopulation], hiddenLayer, outputLayer, epoch,  train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
        # countOriginalLossValue[0][eachPopulation] = accuracy
        # countOriginalLossValue[1][eachPopulation] = local
        # countOriginalLossValue[2][eachPopulation] = precision
        # countOriginalLossValue[3][eachPopulation] = recall
        countOriginalLossValue[0][eachPopulation], model = fitness(populationDataOriginal[eachPopulation], hiddenLayer, outputLayer, epoch,  train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
        originalModel.append(model)

        # accuracy, local, precision, recall = fitness(crossoverData[eachPopulation], hiddenLayer, outputLayer, epoch,  train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
        # countCrossoverLossValue[0][eachPopulation] = accuracy
        # countCrossoverLossValue[1][eachPopulation] = local
        # countCrossoverLossValue[2][eachPopulation] = precision
        # countCrossoverLossValue[3][eachPopulation] = recall
        countCrossoverLossValue[0][eachPopulation], model = fitness(crossoverData[eachPopulation], hiddenLayer, outputLayer, epoch,  train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
        crossoverModel.append(model)

    for eachPopulation in range(np.size(countCrossoverLossValue, 1)):
        if countCrossoverLossValue[0][eachPopulation] <= countOriginalLossValue[0][eachPopulation]:
            for eachDim in range(hiddenLayer):
                selectionPopulationData[eachPopulation][eachDim] = crossoverData[eachPopulation][eachDim]
    return selectionPopulationData