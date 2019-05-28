import torch.nn.functional as F
import torch.nn as nn

class Net(nn.Module):
    def __init__(self, input_dim, output_dim, hiddenLayer, hiddenNeural):
        super(Net, self).__init__()
        self.linears = nn.ModuleList([nn.Linear(input_dim,hiddenNeural[0])])
        for hiddenLayerNumber in range(hiddenLayer):
            if hiddenLayerNumber == hiddenLayer-1:
                self.linears.append(nn.Linear(hiddenNeural[-1], output_dim))
            else:
                self.linears.append(nn.Linear(hiddenNeural[hiddenLayerNumber], hiddenNeural[hiddenLayerNumber+1]))
    
    def forward(self, x, hiddenLayer):                
        for step, network in enumerate(self.linears):
            if step == 0:
                x = F.relu(self.linears[step](x))
            elif step == (2+hiddenLayer-1):
                x = F.relu(self.linears[step](x)) # To check with the loss function
            else:
                x = F.relu(self.linears[step](x))
        return x