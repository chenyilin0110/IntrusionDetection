import numpy as np
from neuralnetwork import Net
import torch.optim as optim
import torch.nn as nn
from accuracyfunction import accuracy

def fitness(data, hiddenLayer, outputLayer, epoch, train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor):
    # build network
    net = Net(np.size(train_noStringTemp_X, 1), outputLayer, hiddenLayer, data)
    
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
    # accuracyvalue, local, precision, recall = accuracy(y_test_tensor, y_test_list_predic)
    accuracyvalue = accuracy(y_test_tensor, y_test_list_predic)
    return accuracyvalue