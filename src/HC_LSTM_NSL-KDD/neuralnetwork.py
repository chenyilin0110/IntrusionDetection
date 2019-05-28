import torch.nn as nn
import torch.nn.functional as F

class LSTM(nn.Module):
    def __init__(self, inputDim, outputDim, neuron):
        super(LSTM, self).__init__()
        
        self.lstm = nn.LSTM(
            input_size = inputDim,
            hidden_size = neuron,
            num_layers = 1,# how many hidden layeri in RNN
        )        
        self.out = nn.Linear(neuron, outputDim)

    def forward(self, x, h, c):
        r_out, (h, c) = self.lstm(x, (h, c))
        out = self.out(r_out)
        return out, (h, c)