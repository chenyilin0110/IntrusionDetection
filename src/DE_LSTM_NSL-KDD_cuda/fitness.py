import numpy as np
from neuralnetwork import LSTM
import torch.optim as optim
import torch.nn as nn
import torch
from accuracyfunction import accuracy
import time
def fitness(data, hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor, cuda):
    # bulid lstm
    lstm = LSTM(np.size(train_noStringTemp_X,1), int(outputLayer), data[0].tolist())
    if cuda == True:
        lstm.cuda()
    
    # set optimizer and lossFunction
    optimizer = optim.Adam(lstm.parameters(), lr=0.05)
    lossFunction = nn.CrossEntropyLoss()

    # split batch
    batch_train_dataset = torch.utils.data.TensorDataset(x_train_tensor, y_train_tensor)
    train_loader = torch.utils.data.DataLoader(batch_train_dataset, batch_size=batchSize, shuffle=True)

    # traning
    for eachepoch in range(int(epoch)):
        for step, (batch_x, batch_y) in enumerate (train_loader):
            batch_x = batch_x.view(1, -1, np.size(train_noStringTemp_X, 1)) # seq_len batch_size input_dim
        
            if cuda == True:
                y_prediction = lstm(batch_x.cuda())
            else:
                y_prediction = lstm(batch_x)

            y_prediction = y_prediction.view(np.size(batch_x.numpy(), 1), -1) # reshape from 3 dimention to 2 dimention
            
            if cuda == True:
                loss = lossFunction(y_prediction, batch_y.cuda())
            else:
                loss = lossFunction(y_prediction, batch_y)
            
            optimizer.zero_grad()# clean optimizer
            loss.backward(retain_graph=True)# calculate new parameters
            optimizer.step()# update parameters
    loss_value = float(loss.item())

    # h = torch.Tensor(1, len(x_test_tensor), data[0].tolist()).zero_()
    # c = torch.Tensor(1, len(x_test_tensor), data[0].tolist()).zero_()

    # x_test = x_test_tensor.view(1, -1, np.size(train_noStringTemp_X, 1))

    # if cuda == True:
    #     y_test_predic, _ = lstm(x_test.cuda(), h.cuda(), c.cuda())
    # else:
    #         y_test_predic, _ = lstm(x_test, h, c)

    # pred = y_test_predic.detach().cpu().numpy()
    # pred = pred.reshape(-1, int(outputLayer))
    # y_test_list_predic = np.argmax(pred, axis=1)
    
    # accuracyvalue = accuracy(y_test_tensor, y_test_list_predic)
    return loss_value, lstm