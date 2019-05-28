from sklearn.model_selection import train_test_split
from torch.autograd import Variable
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
import random as rand
from neuralnetwork import Net
import preprocess
import accuracyfunction
from transactionFunction import transaction
#import matplotlib.pyplot as plt
#import seaborn as sns

# set filename outputLayer testing iteration
finder = sys.argv[1]
filename = sys.argv[2]
outputLayer = sys.argv[3]
hiddenLayer = sys.argv[4]
hiddenNeural = sys.argv[5]
testing = sys.argv[6]
iteration = sys.argv[7]
epoch = sys.argv[8]

# load dataset
if finder == "multi":
    temp = np.loadtxt('../../dataset/IndustrialControlSystem/multiclass/'+filename, dtype=np.str, delimiter=',')
elif int(finder) == 2:
    temp = np.loadtxt('../../dataset/IndustrialControlSystem/2class/'+filename, dtype=np.str, delimiter=',')
elif int(finder) == 3:
    temp = np.loadtxt('../../dataset/IndustrialControlSystem/3class/'+filename, dtype=np.str, delimiter=',')

if finder =="multi":
    noStringTemp = temp[0:,0:] 
else:
    noStringTemp = temp[1:,0:] #[欄,列] and clean top string

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
noStringTemp_X = noStringTemp_X.astype(float)

# split data
x_train, x_test, y_train, y_test = train_test_split(resultNormalize, noStringTemp_Y, test_size = float(testing)/100)

# np->tensor
x_train_tensor = Variable(torch.from_numpy(x_train)).float()
y_train_tensor = Variable(torch.from_numpy(y_train)).long()
x_test_tensor = Variable(torch.from_numpy(x_test)).float()
y_test_tensor = Variable(torch.from_numpy(y_test)).long()

solution = np.zeros(int(hiddenLayer))
solution = solution.astype(int)
for i in range(len(solution)):
    solution[i] = rand.randint(int(outputLayer), int(np.size(noStringTemp_X, 1)))
best = np.zeros(4, dtype=float)

for eachiteration in range(int(iteration)):
    # build network
    net = Net(np.size(noStringTemp_X, 1), int(outputLayer), int(hiddenLayer), solution)
    
    # set optimizer and loss_function
    optimizer = optim.Adam(net.parameters(), lr = 0.01)
    lossFunction = nn.CrossEntropyLoss()

    # calculate parameters
    for eachepoch in range(1,int(epoch)+1):
        y_train_predict = net(x_train_tensor, int(hiddenLayer))# cell net.forward() and return predict    
        loss_train = lossFunction(y_train_predict, y_train_tensor)# calculate loss
    #    if epoch % 100 ==0:
    #        print('epoch',loss_train.item())    
        optimizer.zero_grad()# clean optimizer
        loss_train.backward()# calculate new parameters
        optimizer.step()# update parameters

    # testing 
    y_test_predic = net(x_test_tensor, int(hiddenLayer))
    pred = y_test_predic.detach().numpy()
    y_test_list_predic = np.argmax(pred, axis=1)

    # print(filename, " ", end='')
    accuracy, local, precision, recall = accuracyfunction.accuracy(y_test_tensor, y_test_list_predic)    

    # compare f1score
    if best[1] <= local:        
        best[0] = accuracy
        best[1] = local
        best[2] = precision
        best[3] = recall
        bestSolution = solution.copy()
    else:
        for i in range(np.size(bestSolution)):
            solution[i] = bestSolution[i]
    
    if eachiteration != int(iteration)-1:
        # transaction
        solution = transaction(solution, np.size(noStringTemp_X, 1), int(hiddenLayer))
for i in range(len(best)):
    print(best[i])
    # training 
    # y_train_predict = net(x_train_tensor, int(hiddenLayer))
    # pred = y_train_predict.detach().numpy()
    # y_train_list_predic = np.argmax(pred, axis=1)
    # print("The training accuracy is", accuracyfunction.accuracy(y_train_tensor, y_train_list_predic))
    # print()