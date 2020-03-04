import numpy as np
import random as rand

def crossover(populationDataOriginal, mutationData, CR, Ud, Ld, lrUd, lrLd):
    crossoverPopulationData = populationDataOriginal.copy()
    for eachpopulationData_colum in range(np.size(populationDataOriginal, 0)):
        for eachpopulationData_row in range(np.size(populationDataOriginal, 1)):
            r = rand.random()
            if eachpopulationData_row == 0: # first bit(neurons)
                if r <= CR:
                    crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] = \
                        mutationData[eachpopulationData_colum][eachpopulationData_row]
                if crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] > Ud:
                    crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] = int(Ud - 1)
                elif crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] < Ld:
                    crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] = int(Ld + 1)
            else:
                if r <= CR:
                    crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] = \
                        mutationData[eachpopulationData_colum][eachpopulationData_row]
                if crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] > lrUd:
                    crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] = lrUd
                elif crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] < lrLd:
                    crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] = lrLd
    return crossoverPopulationData