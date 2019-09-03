from Fitness import fitness
import numpy as np

def selection(crossoverModel, originalModel, populationDataOriginal, crossoverData, countOriginalOtherAccuracy, countCrossoverOtherAccuracy, hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor, cuda):
    selectionPopulationData = populationDataOriginal
    
    for eachPopulation in range(np.size(populationDataOriginal,0)):
        # accuracy, local, precision, recall = fitness(populationDataOriginal[eachPopulation], hiddenLayer, outputLayer, epoch,  train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
        # countOriginalOtherAccuracy[0][eachPopulation] = accuracy
        # countOriginalOtherAccuracy[1][eachPopulation] = local
        # countOriginalOtherAccuracy[2][eachPopulation] = precision
        # countOriginalOtherAccuracy[3][eachPopulation] = recall
        countOriginalOtherAccuracy[0][eachPopulation],  model = fitness(populationDataOriginal[eachPopulation], hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor, cuda)
        originalModel.append(model)

        # accuracy, local, precision, recall = fitness(crossoverData[eachPopulation], hiddenLayer, outputLayer, epoch,  train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor)
        # countCrossoverOtherAccuracy[0][eachPopulation] = accuracy
        # countCrossoverOtherAccuracy[1][eachPopulation] = local
        # countCrossoverOtherAccuracy[2][eachPopulation] = precision
        # countCrossoverOtherAccuracy[3][eachPopulation] = recall
        countCrossoverOtherAccuracy[0][eachPopulation], model = fitness(crossoverData[eachPopulation], hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor, cuda)
        crossoverModel.append(model)

    for eachPopulation in range(np.size(countCrossoverOtherAccuracy, 1)):
        if countCrossoverOtherAccuracy[0][eachPopulation] >= countOriginalOtherAccuracy[0][eachPopulation]:
            for eachDim in range(hiddenLayer):
                selectionPopulationData[eachPopulation][eachDim] = crossoverData[eachPopulation][eachDim]
    return selectionPopulationData