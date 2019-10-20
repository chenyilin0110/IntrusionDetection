import torch.nn.functional as F
import torch.nn as nn

class Net(nn.Module):
    def __init__(self, input_dim, output_dim, hiddenLayer, hiddenNeural):
        super(Net, self).__init__()
        self.linears = nn.ModuleList([nn.Linear(input_dim,hiddenNeural)])
        for hiddenLayerNumber in range(hiddenLayer):
            self.linears.append(nn.Linear(hiddenNeural, hiddenNeural))
        self.linears.append(nn.Linear(hiddenNeural, output_dim))
    
    def forward(self, x, hiddenLayer):                
        for step, network in enumerate(self.linears):
            if step == 0:
                x = F.relu(self.linears[step](x))
            elif step == (2+hiddenLayer-1):
                x = F.relu(self.linears[step](x)) # To check with the loss function
            else:
                x = F.relu(self.linears[step](x))
        return x