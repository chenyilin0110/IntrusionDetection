import numpy as np
import torch.nn as nn
import torch
from accuracyfunction import accuracy

def testing(hiddenLayer, outputLayer, x_test_tensor, y_test_tensor, name):
    if name == '0':
        net = torch.load('src/DE_DNN_NSL-KDD/result/DE_DNN_' + outputLayer + '.pkl')
    else:
        net = torch.load('src/DE_DNN_NSL-KDD/result/DE_DNN_' + outputLayer + name + '.pkl')
    y_test_predic = net(x_test_tensor, int(hiddenLayer))
    pred = y_test_predic.detach().numpy()
    y_test_list_predic = np.argmax(pred, axis=1)

    accuracyvalue, precision, recall = accuracy(y_test_tensor, y_test_list_predic)
    print(accuracyvalue, precision, recall)