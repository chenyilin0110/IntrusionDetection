import torch.nn as nn
import torch.nn.functional as F
from sklearn.ensemble import RandomForestClassifier

class SNDAE(nn.Module):
    def __init__(self, inputDim):
        super(SNDAE, self).__init__()
        self.network1 = nn.Sequential(
            nn.Linear(inputDim, 14),
            nn.Linear(14, 28),
            nn.Linear(28, 28),
            nn.Sigmoid(),
        )

        self.network2 = nn.Sequential(
            nn.Linear(28, 14),
            nn.Linear(14, 28),
            nn.Linear(28, 28),
            nn.Sigmoid(),
        )

    
    def forward(self, x):
        ndae1 = self.network1(x)
        ndae2 = self.network2(ndae1)
        return ndae2