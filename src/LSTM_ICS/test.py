from sklearn.model_selection import train_test_split
from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
from Neuralnetwork import LSTM
import preprocess
import accuracyfunction
import time

finder = sys.argv[1]
filename = sys.argv[2]
outputlayer = sys.argv[3]
testing = sys.argv[4]
iteration = sys.argv[5]
batchSize = sys.argv[6]
# number = sys.argv[7]
# finder = 2
# filename = "data1.csv"
# outputlayer = 2
# testing = 20
# iteration = 100
# batchSize = 100

start = time.time()
# load dataset
if finder == "multi":
    temp = np.loadtxt('dataset/multiclass/'+filename, dtype=np.str, delimiter=',')
elif int(finder) == 2:
    temp = np.loadtxt('dataset/2class/'+filename, dtype=np.str, delimiter=',')
elif int(finder) == 3:
    temp = np.loadtxt('dataset/3class/'+filename, dtype=np.str, delimiter=',')

# preprocess
if finder =="multi":
    noStringTemp = temp[0:,0:] 
else:
    noStringTemp = temp[1:,0:] #[欄,列] and clean top string

noStringTemp_X = noStringTemp[0:,0:-1]
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
noStringTemp_X = noStringTemp_X.astype(float)

# bulid lstm
lstm = torch.load('lstm.pkl')

# split traning and testing
x_train, x_test, y_train, y_test = train_test_split(resultNormalize, noStringTemp_Y, test_size = float(testing)/100, random_state=42)

# np->tensor
x_train_tensor = Variable(torch.from_numpy(x_train)).float()
y_train_tensor = Variable(torch.from_numpy(y_train)).long()
x_test_tensor = Variable(torch.from_numpy(x_test)).float()
y_test_tensor = Variable(torch.from_numpy(y_test)).long()

# testing
x_test_tensor = x_test_tensor.view(1, -1, np.size(resultNormalize, 1))
y_test_predic = lstm(x_test_tensor)
pred = y_test_predic.detach().numpy()
pred = pred.reshape(-1, int(outputlayer))
y_test_list_predic = np.argmax(pred, axis=1)

accuracyfunction.accuracy(y_test_tensor, y_test_list_predic)