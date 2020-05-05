from torch.autograd import Variable
from sklearn import svm
# from thundersvm import SVC
import torch
import numpy as np
import sys
import random as rand
import preprocess
from accuracyfunction import accuracy
import time

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing iteration
trainData = sys.argv[1]
testData = sys.argv[2]
outputLayer = sys.argv[3]
c = sys.argv[4]

# can use cuda or not
cuda = torch.cuda.is_available()

# load dataset
train_noStringTemp_X = preprocess.loadDataset(trainData)
test_noStringTemp_X = preprocess.loadDataset(testData)

train_temp = preprocess.originalDataset(trainData)
test_temp = preprocess.originalDataset(testData)

# start preprocess----------------------------------------------------------------------------------------------------------

train_noStringTemp_Y = []
train_noStringTemp_Y = preprocess.distinguishNaturalAttack(train_temp, train_noStringTemp_Y, int(outputLayer))
test_noStringTemp_Y = []
test_noStringTemp_Y = preprocess.distinguishNaturalAttack(test_temp, test_noStringTemp_Y, int(outputLayer))

# list->np
train_noStringTemp_X = np.array(train_noStringTemp_X)
train_noStringTemp_Y = np.array(train_noStringTemp_Y)
test_noStringTemp_X = np.array(test_noStringTemp_X)
test_noStringTemp_Y = np.array(test_noStringTemp_Y)

# duration src_bytes
for i in range(len(train_noStringTemp_X)):
    train_noStringTemp_X[i][0] = preprocess.log(train_noStringTemp_X[i][0])
    train_noStringTemp_X[i][4] = preprocess.log(train_noStringTemp_X[i][4])
    train_noStringTemp_X[i][5] = preprocess.log(train_noStringTemp_X[i][5])

for i in range(len(test_noStringTemp_X)):
    test_noStringTemp_X[i][0] = preprocess.log(test_noStringTemp_X[i][0])
    test_noStringTemp_X[i][4] = preprocess.log(test_noStringTemp_X[i][4])
    test_noStringTemp_X[i][5] = preprocess.log(test_noStringTemp_X[i][5])
    
# normalize
train_resultNormalize = preprocess.normalize(train_noStringTemp_X)
test_resultNormalize = preprocess.normalize(test_noStringTemp_X)

# end preprocess----------------------------------------------------------------------------------------------------------

# build svm
svm = svm.SVC(C=float(c))

# training
svmFit = svm.fit(train_resultNormalize, train_noStringTemp_Y)

# testing 
y_test_prediction = svm.predict(test_resultNormalize)

accuracy_value = accuracy(test_noStringTemp_Y, y_test_prediction)
print(accuracy_value)