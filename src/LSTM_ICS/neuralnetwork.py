import torch.nn as nn
import torch.nn.functional as F

class LSTM(nn.Module):
    def __init__(self, inputDim, outputDim):
        super(LSTM, self).__init__()
        
        self.lstm = nn.LSTM(
            input_size = inputDim,
            hidden_size = 64,
            num_layers = 1,# how many hidden layeri in RNN
        )        
        self.out = nn.Linear(64, outputDim)

    def forward(self, x):
        r_out, _ = self.lstm(x)
        out = self.out(r_out)
        return out