import numpy as np
import torch.nn as nn
import torch
from accuracyfunction import accuracy

def testing(outputLayer, x_test_tensor, y_test_tensor, hiddenLayer):
    net = torch.load('src/HC_DNN_NSL-KDD/result/HC_DNN_' + outputLayer + '.pkl')

    # testing
    y_test_predic = net(x_test_tensor, hiddenLayer)
    pred = y_test_predic.detach().numpy()
    y_test_list_predic = np.argmax(pred, axis=1)

    accuracy_value = accuracy(y_test_tensor, y_test_list_predic)
    print(accuracy_value)