import numpy as np
import random as rand

def mutation(populationData, F, Ud, Ld, Lr_Ud, Lr_Ld):    
    oldPopulationData = populationData.copy()
    for eachpopulation_colum in range(np.size(populationData, 0)):
        r1 = rand.randint(0, np.size(populationData, 0)-1) # np.size(populationData,0) = population; but this begin 0
        r2 = rand.randint(0, np.size(populationData, 0)-1)
        while r1==eachpopulation_colum or r2==eachpopulation_colum or r1==r2:
            if r1==eachpopulation_colum:
                r1 = rand.randint(0, np.size(populationData, 0)-1)
            elif r2==eachpopulation_colum:
                r2 = rand.randint(0, np.size(populationData, 0)-1)
            elif r1==r2:
                r1 = rand.randint(0, np.size(populationData, 0)-1)
        for eachpopulation_row in range(np.size(populationData,1)):
            if eachpopulation_row == 0: 
                # mutation neurons
                populationData[eachpopulation_colum][eachpopulation_row] = oldPopulationData[eachpopulation_colum][eachpopulation_row] + \
                    F * (oldPopulationData[r1][eachpopulation_row] - oldPopulationData[r2][eachpopulation_row])
                if populationData[eachpopulation_colum][eachpopulation_row] >= Ud:
                    populationData[eachpopulation_colum][eachpopulation_row] = Ud - 1
                elif populationData[eachpopulation_colum][eachpopulation_row] <= Ld:
                    populationData[eachpopulation_colum][eachpopulation_row] = Ld + 1
            elif eachpopulation_row == 1:
                # mutation learning rate
                populationData[eachpopulation_colum][eachpopulation_row] = oldPopulationData[eachpopulation_colum][eachpopulation_row] + \
                    F * (oldPopulationData[r1][eachpopulation_row] - oldPopulationData[r2][eachpopulation_row])
                if populationData[eachpopulation_colum][eachpopulation_row] >= Lr_Ud:
                    populationData[eachpopulation_colum][eachpopulation_row] = Lr_Ud
                elif populationData[eachpopulation_colum][eachpopulation_row] <= Lr_Ld:
                    populationData[eachpopulation_colum][eachpopulation_row] = Lr_Ld

    return populationData