import numpy as np
import torch.nn as nn
import torch
from accuracyfunction import accuracy

def testing(outputLayer, hiddenLayer, x_test_tensor, y_test_tensor, number):
    net = torch.load('src/DE_DNN_ICS/result/DE_DNN_' + outputLayer + '-' + number + '.pkl')

    y_test_predic = net(x_test_tensor, int(hiddenLayer))
    pred = y_test_predic.detach().numpy()
    y_test_list_predic = np.argmax(pred, axis=1)
    
    accuracyValue = accuracy(y_test_tensor, y_test_list_predic)
    print("ACC", accuracyValue)