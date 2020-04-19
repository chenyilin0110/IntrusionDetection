import torch.nn as nn
import torch.nn.functional as F

class DeepAutoEncoder(nn.Module):
    def __init__(self, inputDim, outputDim):
        super(DeepAutoEncoder, self).__init__()
        
        self.encoder = nn.Sequential(
            nn.Linear(inputDim, 64),
            nn.Tanh(),
            nn.Linear(64, 32),
            nn.Tanh(),
            nn.Linear(32, 8),
            nn.Tanh(),
            nn.Linear(8, 2),
        )

        self.decoder = nn.Sequential(
            nn.Linear(2, 4),
            nn.Tanh(),
            nn.Linear(4, outputDim),
            nn.Sigmoid(),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        
        return decoded