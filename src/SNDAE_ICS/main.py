from sklearn.model_selection import train_test_split
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
finder = sys.argv[1]
filename = sys.argv[2]
outputLayer = sys.argv[3]
test = sys.argv[4]
tree_number = sys.argv[5]
number = sys.argv[6]

# load dataset
noStringTemp = preprocess.load(finder, filename)
noStringTemp_X = noStringTemp[0:,0:-1]

# preprocess
noStringTemp_X = preprocess.missingValue(noStringTemp_X)
if finder != "multi":
    noStringTemp_Y = []
    noStringTemp_Y = preprocess.distinguishNaturalAttack(noStringTemp, noStringTemp_Y)
    # list->np
    noStringTemp_Y = np.array(noStringTemp_Y)    
else:
    noStringTemp_Y = noStringTemp[:,-1]    
    noStringTemp_Y = noStringTemp_Y.astype(int)
    # multiclass 1 to 41, but lossfunction from 0 begin
    for i in range(len(noStringTemp_Y)):
        noStringTemp_Y[i] -= 1

resultNormalize = preprocess.normalize(noStringTemp_X)

# np->tensor but noStringTemp_X is not float so astype(x)
noStringTemp_X = noStringTemp_X.astype(float)

# split data
x_train, x_test, y_train, y_test = train_test_split(resultNormalize, noStringTemp_Y, test_size = float(test)/100)

# np->tensor
x_train_tensor = Variable(torch.from_numpy(x_train)).float()
y_train_tensor = Variable(torch.from_numpy(y_train)).long()
x_test_tensor = Variable(torch.from_numpy(x_test)).float()
y_test_tensor = Variable(torch.from_numpy(y_test)).long()

# end preprocess----------------------------------------------------------------------------------------------------------

# bulid autoencoder
sndae = SNDAE(np.size(x_train,1))
random_forest = RandomForestClassifier(n_estimators=int(tree_number), n_jobs=-1)

# set optimizer and lossFunction
optimizer = optim.RMSprop(sndae.parameters(), lr=0.05)
lossFunction = nn.CrossEntropyLoss()

# traning
sndae_train = sndae(x_train_tensor)
sndae_train = sndae_train.data.numpy() # tensor to numpy
random_forest = random_forest.fit(sndae_train, y_train)

# testing
sndae_test = sndae(x_test_tensor)
sndae_test = sndae_test.data.numpy()
y_test_predic = random_forest.predict(sndae_test)

accuracy, precision, recall = accuracy(y_test, y_test_predic)
print(accuracy, precision, recall)
torch.save(sndae, 'src/SNDAE_ICS/result/sndae' + outputLayer + '-' + number + '.pkl')
torch.save(random_forest, 'src/SNDAE_ICS/result/rf' + outputLayer + '-' + number + '.pkl')