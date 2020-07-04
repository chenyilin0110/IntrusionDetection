from torch.autograd import Variable
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

# load dataset
train_noStringTemp_X = preprocess.loadDataset(trainData)
test_noStringTemp_X = preprocess.loadDataset(testData)

train_temp = preprocess.originalDataset(trainData)
test_temp = preprocess.originalDataset(testData)

train_noStringTemp_Y = []
train_noStringTemp_Y = preprocess.distinguishNaturalAttack(train_temp, train_noStringTemp_Y, int(outputLayer))
test_noStringTemp_Y = []
test_noStringTemp_Y = preprocess.distinguishNaturalAttack(test_temp, test_noStringTemp_Y, int(outputLayer))

# list->np
train_noStringTemp_Y = np.array(train_noStringTemp_Y)
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

# bulid autoencoder
sndae = SNDAE(np.size(train_noStringTemp_X,1))
random_forest = RandomForestClassifier(n_estimators=int(tree_number), n_jobs=-1)

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
torch.save(sndae, 'src/SNDAE_KDD99/result/sndae' + outputLayer + '.pkl')
torch.save(random_forest, 'src/SNDAE_KDD99/result/sndae' + outputLayer + '.pkl')