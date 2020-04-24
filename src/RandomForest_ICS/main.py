from sklearn.model_selection import train_test_split
from sklearn import ensemble
from torch.autograd import Variable
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
import preprocess
import accuracyfunction
# import matplotlib.pyplot as plt
#import seaborn as sns

# set filename outputLayer testing iteration
finder = sys.argv[1]
filename = sys.argv[2]
outputLayer = sys.argv[3]
testing = sys.argv[4]

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

# build random forset
forest = ensemble.RandomForestClassifier(n_estimators=100)

# split data
x_train, x_test, y_train, y_test = train_test_split(resultNormalize, noStringTemp_Y, test_size = float(testing)/100)

# training
forestFit = forest.fit(x_train, y_train)

# testing
y_test_prediction = forest.predict(x_test)

accuracyValue = accuracyfunction.accuracy(y_test, y_test_prediction)
print(accuracyValue)