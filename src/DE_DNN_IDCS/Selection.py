from Fitness import fitness
import numpy as np

def selection(populationDataOriginal, crossoverData, countOriginalOtherAccuracy, countCrossoverOtherAccuracy, hiddenLayer, outputLayer, epoch, noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor):
    selectionPopulationData = populationDataOriginal
    
    for eachPopulation in range(np.size(populationDataOriginal,0)):
        accuracy, local, precision, recall = fitness(populationDataOriginal[eachPopulation], hiddenLayer, outputLayer, epoch,  noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
        countOriginalOtherAccuracy[0][eachPopulation] = accuracy
        countOriginalOtherAccuracy[1][eachPopulation] = local
        countOriginalOtherAccuracy[2][eachPopulation] = precision
        countOriginalOtherAccuracy[3][eachPopulation] = recall

        accuracy, local, precision, recall = fitness(crossoverData[eachPopulation], hiddenLayer, outputLayer, epoch,  noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
        countCrossoverOtherAccuracy[0][eachPopulation] = accuracy
        countCrossoverOtherAccuracy[1][eachPopulation] = local
        countCrossoverOtherAccuracy[2][eachPopulation] = precision
        countCrossoverOtherAccuracy[3][eachPopulation] = recall

    for eachPopulation in range(np.size(countCrossoverOtherAccuracy, 1)):
        if countCrossoverOtherAccuracy[1][eachPopulation] >= countOriginalOtherAccuracy[1][eachPopulation]:
            for eachDim in range(hiddenLayer):
                selectionPopulationData[eachPopulation][eachDim] = crossoverData[eachPopulation][eachDim]
    return selectionPopulationData