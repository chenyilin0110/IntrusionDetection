from sklearn.model_selection import train_test_split
from torch.autograd import Variable
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
from neuralnetwork import Net
import preprocess
import accuracyfunction
#import matplotlib.pyplot as plt
#import seaborn as sns

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing epoch

week = sys.argv[1]
outputLayer = sys.argv[2]
hiddenLayer = sys.argv[3]
hiddenNeural = sys.argv[4]
epoch = sys.argv[5]


# load dataset
data = preprocess.load(week)
print("總筆數：", len(data))
print(data)
# duration_list = []
protocal_list = []
source_ip_list = []
# source_port_list = []
distination_ip_list = []
# distination_port_list = []
# packets_list = []
# byte_list = []
flag_list = []

protocal, source_ip, distination_ip, flag = preprocess.onehotencoding(data, \
            protocal_list, source_ip_list, distination_ip_list, flag_list)
data = data.values
preprocess.replace(data, protocal_list, protocal, source_ip_list, source_ip, \
distination_ip_list, distination_ip, flag_list, flag)
# # preprocess
# train_x = train_data[:,0:-1]
# test_x = test_data[:,0:-1]
# train_y = []
# test_y = []
# preprocess.distinguishNaturalAttack(train_data, train_y)
# preprocess.distinguishNaturalAttack(test_data, test_y)

# # list to np
# train_y = np.array(train_y)
# test_y = np.array(test_y)

# # np string to float
# train_x = train_x.astype(np.float)
# train_y = train_y.astype(np.float)
# test_x = test_x.astype(np.float)
# test_y = test_y.astype(np.float)
# # build network
# net = Net(np.size(train_x,1), int(outputLayer), int(hiddenLayer), int(hiddenNeural))

# # set optimizer and loss_function
# optimizer = optim.Adam(net.parameters(), lr = 0.01)
# lossFunction = nn.CrossEntropyLoss()

# # np->tensor
# x_train_tensor = Variable(torch.from_numpy(train_x)).float()
# y_train_tensor = Variable(torch.from_numpy(train_y)).long()
# x_test_tensor = Variable(torch.from_numpy(test_x)).float()
# y_test_tensor = Variable(torch.from_numpy(test_y)).long()

# # calculate parameters
# for eachepoch in range(1,int(epoch)+1):
#     y_train_predict = net(x_train_tensor, int(hiddenLayer))# cell net.forward() and return predict    
#     loss_train = lossFunction(y_train_predict, y_train_tensor)# calculate loss
# #    if epoch % 100 ==0:
# #        print('epoch',loss_train.item())    
#     optimizer.zero_grad()# clean optimizer
#     loss_train.backward()# calculate new parameters
#     optimizer.step()# update parameters

# # testing 
# y_test_predic = net(x_test_tensor, int(hiddenLayer))
# pred = y_test_predic.detach().numpy()#training's cannot impact testing
# y_test_list_predic = np.argmax(pred, axis=1)

# accuracyfunction.accuracy(y_test_tensor, y_test_list_predic)