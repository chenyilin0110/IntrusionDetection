import numpy as np
import torch.nn as nn
import torch
from accuracyfunction import accuracy

def testing(outputLayer, train_resultNormalize, x_test_tensor, y_test_tensor, cuda, name):
    if name == '0':
        lstm = torch.load('src/HC_LSTM_NSL-KDD/result/HC_LSTM_' + outputLayer + '.pkl')
    else:
        lstm = torch.load('src/HC_LSTM_NSL-KDD/result/HC_LSTM_' + outputLayer + name +'.pkl')
    # testing
    x_test = x_test_tensor.view(1, -1, np.size(train_resultNormalize, 1))
    
    y_test_predic = lstm(x_test.cuda())

    if cuda == True:
        pred = y_test_predic.detach().cpu().numpy()
    else:
        pred = y_test_predic.detach().numpy()
    
    pred = pred.reshape(-1, int(outputLayer))
    y_test_list_predic = np.argmax(pred, axis=1)
    
    accuracy_value = accuracy(y_test_tensor, y_test_list_predic)
    
    print(accuracy_value)