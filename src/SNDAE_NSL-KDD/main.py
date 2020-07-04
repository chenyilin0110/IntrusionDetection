from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import sys
from neuralnetwork import SNDAE
import preprocess
from accuracyfunction import accuracy
import time
from sklearn.ensemble import RandomForestClassifier

# don't show warnings message
import warnings
warnings.filterwarnings("ignore")

# set filename outputLayer testing iteration
trainData = sys.argv[1]
testData = sys.argv[2]
outputLayer = sys.argv[3]
tree_number = sys.argv[4]
learning_rate = sys.argv[5]
name = sys.argv[6]

# load trainData
train_temp = preprocess.loadDataset(trainData)
train_noStringTemp_X = train_temp[0:,0:-1]

# start preprocess----------------------------------------------------------------------------------------------------------

# only trainData do this
protocal_type_list = preprocess.saveProtocal_typeOrder(train_noStringTemp_X)
service_list = preprocess.saveServiceOrder(train_noStringTemp_X)
flag_list = preprocess.saveFlagOrder(train_noStringTemp_X)
protocal_type_onehotencoded = preprocess.onehotencoded(protocal_type_list)
service_list_onehotencoded = preprocess.onehotencoded(service_list)
flag_list_onehotencoded = preprocess.onehotencoded(flag_list)

# load testData
test_temp = preprocess.loadDataset(testData)
test_noStringTemp_X = test_temp[0:,0:-1]

train_noStringTemp_Y = []
train_noStringTemp_Y = preprocess.distinguishNaturalAttack(train_temp, train_noStringTemp_Y, int(outputLayer))
test_noStringTemp_Y = []
test_noStringTemp_Y = preprocess.distinguishNaturalAttack(test_temp, test_noStringTemp_Y, int(outputLayer))

# np can't dynamic add number so use list
train_noStringTemp_X = train_noStringTemp_X.tolist() 
test_noStringTemp_X = test_noStringTemp_X.tolist()

# replace text with onehotencoded number
preprocess.replace(train_noStringTemp_X, protocal_type_list, service_list, flag_list, protocal_type_onehotencoded, service_list_onehotencoded, flag_list_onehotencoded)
preprocess.replace(test_noStringTemp_X, protocal_type_list, service_list, flag_list, protocal_type_onehotencoded, service_list_onehotencoded, flag_list_onehotencoded)

# list->np
train_noStringTemp_X = np.array(train_noStringTemp_X)
train_noStringTemp_Y = np.array(train_noStringTemp_Y)
test_noStringTemp_X = np.array(test_noStringTemp_X)
test_noStringTemp_Y = np.array(test_noStringTemp_Y)

# duration src_bytes
for i in range(len(train_noStringTemp_X)):
    train_noStringTemp_X[i][0] = preprocess.log(train_noStringTemp_X[i][0])
    train_noStringTemp_X[i][4] = preprocess.log(train_noStringTemp_X[i][4])
    train_noStringTemp_X[i][5] = preprocess.log(train_noStringTemp_X[i][5])

for i in range(len(test_noStringTemp_X)):
    test_noStringTemp_X[i][0] = preprocess.log(test_noStringTemp_X[i][0])
    test_noStringTemp_X[i][4] = preprocess.log(test_noStringTemp_X[i][4])
    test_noStringTemp_X[i][5] = preprocess.log(test_noStringTemp_X[i][5])

# normalize
train_resultNormalize = preprocess.normalize(train_noStringTemp_X)
test_resultNormalize = preprocess.normalize(test_noStringTemp_X)

# np->tensor
x_train_tensor = Variable(torch.from_numpy(train_resultNormalize)).float()
y_train_tensor = Variable(torch.from_numpy(train_noStringTemp_Y)).long()
x_test_tensor = Variable(torch.from_numpy(test_resultNormalize)).float()
y_test_tensor = Variable(torch.from_numpy(test_noStringTemp_Y)).long()

# end preprocess----------------------------------------------------------------------------------------------------------

# bulid stacked non-symmetric deep auto encoder model & random forest
sndae = SNDAE(np.size(train_resultNormalize,1))
random_forest = RandomForestClassifier(n_estimators=int(tree_number),n_jobs=-1)

# set optimizer and lossFunction
optimizer = optim.RMSprop(sndae.parameters(), lr=float(learning_rate))
lossFunction = nn.CrossEntropyLoss()

# traning
sndae_train = sndae(x_train_tensor)
sndae_train = sndae_train.data.numpy() # tensor to numpy
random_forest = random_forest.fit(sndae_train, train_noStringTemp_Y)
 
# testing
sndae_test = sndae(x_test_tensor)
sndae_test = sndae_test.data.numpy()
y_test_predic = random_forest.predict(sndae_test)

accuracy, precision, recall = accuracy(test_noStringTemp_Y, y_test_predic)
print(accuracy, precision, recall)
if name == "0":
    torch.save(sndae, 'src/SNDAE_NSL-KDD/result/sndae' + outputLayer + '.pkl')
    torch.save(random_forest, 'src/SNDAE_NSL-KDD/result/rf' + outputLayer + '.pkl')
else:
    torch.save(sndae, 'src/SNDAE_NSL-KDD/result/sndae' + outputLayer + name + '.pkl')
    torch.save(random_forest, 'src/SNDAE_NSL-KDD/result/rf' + outputLayer + name + '.pkl')