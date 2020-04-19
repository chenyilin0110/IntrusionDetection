import numpy as np
import random as rand

def update(best, bestModel, eachiteration, bestSolution, eachIterationLocalBest, population, countCrossoverLossValue, countOriginalLossValue, crossoverModel, originalModel, selectionData):
    
    if eachiteration == 0:
        best = countCrossoverLossValue[0][0]
        bestModel = crossoverModel[0]

    for i in range(np.size(countCrossoverLossValue, 1)):
        # if best <= countCrossoverLossValue[1][i]:
            # best = countCrossoverLossValue[1][i
        if best >= countCrossoverLossValue[0][i]:
            best = countCrossoverLossValue[0][i]
            bestModel = crossoverModel[i]
            # bestAccuracy = countCrossoverLossValue[0][i]
            # bestPrecision = countCrossoverLossValue[2][i]
            # bestRecall = countCrossoverLossValue[3][i]
            for j in range(len(bestSolution)):
                bestSolution[j] = selectionData[i][j]

    for i in range(np.size(countCrossoverLossValue, 1)):
        # if best <= countOriginalLossValue[1][i]:
        #     best = countOriginalLossValue[1][i]
        if best >= countOriginalLossValue[0][i]:
            best = countOriginalLossValue[0][i]
            bestModel = originalModel[i]
            # bestAccuracy = countOriginalLossValue[0][i]
            # bestPrecision = countOriginalLossValue[2][i]
            # bestRecall = countOriginalLossValue[3][i]
            for j in range(len(bestSolution)):
                bestSolution[j] = selectionData[i][j]
    
    eachIterationLocalBest.append(bestSolution[0]) # save each iteration best local
    index = 0
    count = 0
    total = 0
    if eachiteration >= 4:
        for j in range(len(eachIterationLocalBest)):
            if eachIterationLocalBest[index] != eachIterationLocalBest[j]:
                count = 0
                index = j
                count += 1
            else:
                count +=1
        
        if count >= 5: # five iteration same
            for i in range(len(eachIterationLocalBest)):
                total += eachIterationLocalBest[i]
            total /= (eachiteration + 1)

            # reset
            ran = rand.randint(0, int(population)-1)
            populationDataOriginal = selectionData.copy()
            populationData = selectionData.copy()
            populationDataOriginal[ran] = int(total)
            populationData[ran] = int(total)
    else:    
        # reset
        populationDataOriginal = selectionData.copy()
        populationData = selectionData.copy()
    print(best)
    return best, bestModel