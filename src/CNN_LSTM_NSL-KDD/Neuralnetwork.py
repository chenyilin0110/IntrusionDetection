import torch.nn as nn
import torch.nn.functional as F
import torch as t
import numpy as np
class CNN(nn.Module):
    def __init__(self, inputDim, outputDim):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            # how many layer in input
            nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
        )
        
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=1, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=1, stride=2),
        )
        
        self.lstm = nn.LSTM(
            input_size = int(inputDim/2),
            hidden_size = 32,
            num_layers = 1,# how many hidden layeri in RNN
        )        
        self.out = nn.Linear(32, outputDim)
    
    def forward(self, x, lstm_input):
        out = self.conv1(x)
        out = self.conv2(out)
        out = out.view(-1, 1, int(lstm_input/2))
        r_out, _ = self.lstm(out)
        out = self.out(r_out)
        return out