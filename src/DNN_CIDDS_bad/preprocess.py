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
        if original[i,-1] == '1.000000':
            y.append(0)
        elif original[i,-1] == '2.000000':
            y.append(1)
        elif original[i,-1] == '3.000000':
            y.append(2)
        elif original[i,-1] == '4.000000':
            y.append(3)
        elif original[i,-1] == '5.000000':
            y.append(4)
    return y

def normalize(x):
    temp = x    
    temp = temp.astype(float)
    result = preprocessing.scale(temp)    
    return result