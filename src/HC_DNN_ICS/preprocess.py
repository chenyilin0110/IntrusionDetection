from sklearn import preprocessing
import numpy as np

def missingValue(x):
    for i in range(np.size(x,0)):
        for j in range(np.size(x,1)):
            if x[i][j] == 'inf':
                x[i][j] = 0
            elif x[i][j] == 'nan':
                x[i][j] = 0
    return x        
        
def distinguishNaturalAttack(original, y):
# Natural->0 Attack->1
    for i in range(np.size(original,0)):
        if original[i,-1] == 'Natural':
            y.append(0)
        elif original[i,-1] == 'Attack':
            y.append(1)
        elif original[i,-1] == 'NoEvents':
            y.append(2)
    return y

def normalize(x):
    temp = x    
    temp = temp.astype(float)
    result = preprocessing.scale(temp)    
    return result