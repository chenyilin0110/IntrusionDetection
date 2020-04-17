import numpy as np
from neuralnetwork import Net
import torch.optim as optim
import torch.nn as nn

def fitness(data, hiddenLayer, outputLayer, epoch, noStringTemp_X, x_train_tensor, y_train_tensor):
    # build network
    net = Net(np.size(noStringTemp_X, 1), outputLayer, hiddenLayer, data)
    
    # set optimizer and loss_function
    optimizer = optim.Adam(net.parameters(), lr = 0.01)
    lossFunction = nn.CrossEntropyLoss()

    # calculate parameters
    for eachepoch in range(epoch):
        loss_value = 0.0
        y_train_predict = net(x_train_tensor, int(hiddenLayer))# cell net.forward() and return predict    
        loss_train = lossFunction(y_train_predict, y_train_tensor)# calculate loss
    #    if epoch % 100 ==0:
    #        print('epoch',loss_train.item())    
        optimizer.zero_grad()# clean optimizer
        loss_train.backward()# calculate new parameters
        optimizer.step()# update parameters
        
        if eachepoch == epoch-1:
            loss_value = float(loss_train.item())

    return loss_value, net