from sklearn.model_selection import train_test_split
from sklearn import svm
from torch.autograd import Variable
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
import preprocess
import accuracyfunction
#import matplotlib.pyplot as plt
#import seaborn as sns

# set filename outputLayer testing iteration
finder = sys.argv[1]
filename = sys.argv[2]
outputLayer = sys.argv[3]
testing = sys.argv[4]
c = sys.argv[5]

# load dataset
noStringTemp = preprocess.load(finder, filename)
noStringTemp_X = noStringTemp[0:,0:-1]

# preprocess
noStringTemp_X = preprocess.missingValue(noStringTemp_X)
if finder != "multi":
    noStringTemp_Y = []
    noStringTemp_Y = preprocess.distinguishNaturalAttack(noStringTemp, noStringTemp_Y)
    # list->np
    noStringTemp_Y = np.array(noStringTemp_Y)    
else:
    noStringTemp_Y = noStringTemp[:,-1]    
    noStringTemp_Y = noStringTemp_Y.astype(int)
    # multiclass 1 to 41, but lossfunction from 0 begin
    for i in range(len(noStringTemp_Y)):
        noStringTemp_Y[i] -= 1

resultNormalize = preprocess.normalize(noStringTemp_X)

# np->tensor but noStringTemp_X is not float so astype(x)
# noStringTemp_X = noStringTemp_X.astype(float)

# build svm
svm = svm.SVC(C=float(c))

# split data
x_train, x_test, y_train, y_test = train_test_split(resultNormalize, noStringTemp_Y, test_size = float(testing)/100)

# training
svmFit = svm.fit(x_train, y_train)

# testing 
y_test_prediction = svm.predict(x_test)

accuracyValue, precision, recall = accuracyfunction.accuracy(y_test, y_test_prediction)
print(accuracyValue, precision, recall)