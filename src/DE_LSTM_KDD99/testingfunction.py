import numpy as np
import torch.nn as nn
import torch
from accuracyfunction import accuracy

def testing(outputLayer, train_noStringTemp_X, x_test_tensor, y_test_tensor, cuda, batchSize, number):
    lstm = torch.load('src/DE_LSTM_KDD99/result/DE_LSTM_' + outputLayer + '_bs' + batchSize + '-' + number + '.pkl')
    
    x_test = x_test_tensor.view(1, -1, np.size(train_noStringTemp_X, 1))

    if cuda == True:
        y_test_predic = lstm(x_test.cuda())
        pred = y_test_predic.detach().cpu().numpy()
    else:
        y_test_predic = lstm(x_test)
        pred = y_test_predic.detach().numpy()

    pred = pred.reshape(-1, int(outputLayer))
    y_test_list_predic = np.argmax(pred, axis=1)
    
    accuracyvalue = accuracy(y_test_tensor, y_test_list_predic)
    print(accuracyvalue)