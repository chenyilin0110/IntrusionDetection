import numpy as np
import random as rand

def update(best, bestModel, eachiteration, bestSolution, eachIterationLocalBest, population, countCrossoverLossValue, countOriginalLossValue, crossoverModel, originalModel, selectionData, name):
    if eachiteration == 0:
        best = countCrossoverLossValue[0][0]
        bestModel = crossoverModel[0]

    for i in range(np.size(countCrossoverLossValue, 1)):
        if best >= countCrossoverLossValue[0][i]:
            best = countCrossoverLossValue[0][i]
            bestModel = crossoverModel[i]
            for j in range(len(bestSolution)):
                bestSolution[j] = selectionData[i][j]

    for i in range(np.size(countCrossoverLossValue, 1)):
        if best >= countOriginalLossValue[0][i]:
            best = countOriginalLossValue[0][i]
            bestModel = originalModel[i]
            for j in range(len(bestSolution)):
                bestSolution[j] = selectionData[i][j]

    # save each iteration best local
    for i in range(np.size(eachIterationLocalBest, 1)):
        if i == 0:
            eachIterationLocalBest[eachiteration][i] = best
        else:
            eachIterationLocalBest[eachiteration][i] = bestSolution[i-1]
    
    if eachiteration >= 4:
        index = 0
        count = 0
        total = np.zeros(len(bestSolution),dtype=float)
    
        for j in range(eachiteration+1):
            if eachIterationLocalBest[index][0] != eachIterationLocalBest[j][0]: # [0]-> acc [1]&[2]-> parameters
                count = 0
                index = j
                count += 1
            else:
                count +=1
        
        if count >= 5: # five iteration same
            for i in range(eachiteration):
                total[0] += eachIterationLocalBest[i][1]
                total[1] += eachIterationLocalBest[i][2]
            total[0] /= (eachiteration + 1)
            total[1] /= (eachiteration + 1)
            
            # reset
            ran = rand.randint(0, int(population)-1)
            populationDataOriginal = selectionData.copy()
            populationData = selectionData.copy()
            for i in range(len(bestSolution)):
                populationDataOriginal[ran][i] = total[i]
                populationData[ran][i] = total[i]
    else:    
        # reset
        populationDataOriginal = selectionData.copy()
        populationData = selectionData.copy()
    print(best, 'neurons', bestSolution[0], 'lr', bestSolution[1])
    return best, bestModel