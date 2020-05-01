import numpy as np
import torch.nn as nn
import torch
from accuracyfunction import accuracy

def testing(outputLayer, hiddenLayer, train_noStringTemp_X, x_test_tensor, y_test_tensor, cuda, number):
    net = torch.load('src/DE_DNN_KDD99/result/DE_DNN_' + outputLayer + '-' + number + '.pkl')
    
    x_test = x_test_tensor.view(1, -1, np.size(train_noStringTemp_X, 1))

    if cuda == True:
        y_test_predic = net(x_test.cuda(), int(hiddenLayer))
        pred = y_test_predic.detach().cpu().numpy()
    else:
        y_test_predic = net(x_test, int(hiddenLayer))
        pred = y_test_predic.detach().numpy()

    pred = pred.reshape(-1, int(outputLayer))
    y_test_list_predic = np.argmax(pred, axis=1)
    
    accuracyvalue = accuracy(y_test_tensor, y_test_list_predic)
    print(accuracyvalue)