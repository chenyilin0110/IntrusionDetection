import numpy as np
import random as rand

def crossover(populationDataOriginal, mutationData, CR1, CR2, CR3, Ud, Ld, lrUd, lrLd):
    crossoverData = np.zeros((np.size(populationDataOriginal, 0), 5, np.size(populationDataOriginal, 1)))
    crossoverPopulationData = populationDataOriginal.copy()
    
    for eachpopulationData_colum in range(np.size(populationDataOriginal, 0)):
        for eachpopulationData_row in range(np.size(populationDataOriginal, 1)):
            r = rand.random()
            if eachpopulationData_row == 0: # first bit(neurons)
                # Uj1
                if r <= CR1:
                    crossoverData[eachpopulationData_colum][0][eachpopulationData_row] = \
                        mutationData[eachpopulationData_colum][eachpopulationData_row]
                else:
                    crossoverData[eachpopulationData_colum][0][eachpopulationData_row] = \
                        crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]
                # Uj2
                if r <= CR2:
                    crossoverData[eachpopulationData_colum][1][eachpopulationData_row] = \
                        mutationData[eachpopulationData_colum][eachpopulationData_row]
                else:
                    crossoverData[eachpopulationData_colum][1][eachpopulationData_row] = \
                        crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]
                # Uj3
                if r <= CR3:
                    crossoverData[eachpopulationData_colum][2][eachpopulationData_row] = \
                        mutationData[eachpopulationData_colum][eachpopulationData_row]
                else:
                    crossoverData[eachpopulationData_colum][2][eachpopulationData_row] = \
                        crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]
                # Uj4
                crossoverData[eachpopulationData_colum][3][eachpopulationData_row] = \
                    r * crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]
                # Uj5
                crossoverData[eachpopulationData_colum][4][eachpopulationData_row] = \
                    r * mutationData[eachpopulationData_colum][eachpopulationData_row] + \
                        (1 - r) * crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]

                for each in range(np.size(crossoverData, 1)):
                    if crossoverData[eachpopulationData_colum][each][eachpopulationData_row] > Ud:
                        crossoverData[eachpopulationData_colum][each][eachpopulationData_row] = int(Ud - 1)
                    elif crossoverData[eachpopulationData_colum][each][eachpopulationData_row] < Ld:
                        crossoverData[eachpopulationData_colum][each][eachpopulationData_row] = int(Ld + 1)
            else:
                # Uj1
                if r <= CR1:
                    crossoverData[eachpopulationData_colum][0][eachpopulationData_row] = \
                        mutationData[eachpopulationData_colum][eachpopulationData_row]
                else:
                    crossoverData[eachpopulationData_colum][0][eachpopulationData_row] = \
                        crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]
                # Uj2
                if r <= CR2:
                    crossoverData[eachpopulationData_colum][1][eachpopulationData_row] = \
                        mutationData[eachpopulationData_colum][eachpopulationData_row]
                else:
                    crossoverData[eachpopulationData_colum][1][eachpopulationData_row] = \
                        crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]
                # Uj3
                if r <= CR3:
                    crossoverData[eachpopulationData_colum][2][eachpopulationData_row] = \
                        mutationData[eachpopulationData_colum][eachpopulationData_row]
                else:
                    crossoverData[eachpopulationData_colum][2][eachpopulationData_row] = \
                        crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]
                # Uj4
                crossoverData[eachpopulationData_colum][3][eachpopulationData_row] = \
                    r * crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]
                # Uj5
                crossoverData[eachpopulationData_colum][4][eachpopulationData_row] = \
                    r * mutationData[eachpopulationData_colum][eachpopulationData_row] + \
                        (1 - r) * crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row]

                for each in range(np.size(crossoverData, 1)):
                    if crossoverData[eachpopulationData_colum][each][eachpopulationData_row] > lrUd:
                        crossoverData[eachpopulationData_colum][each][eachpopulationData_row] = lrUd
                    elif crossoverData[eachpopulationData_colum][each][eachpopulationData_row] < lrLd:
                        crossoverData[eachpopulationData_colum][each][eachpopulationData_row] = lrLd
    return crossoverData