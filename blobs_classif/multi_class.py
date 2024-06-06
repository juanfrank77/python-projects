# Multi-class classification model 

import torch
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
import torch.nn as nn

NUM_CLASSES = 4
NUM_FEATURES = 2
RANDOM_SEED = 42

x_blob, y_blob = datasets.make_blobs(n_samples=1000, n_features=NUM_FEATURES, centers=NUM_CLASSES, cluster_std=1.5, random_state=RANDOM_SEED)

x_blob = torch.from_numpy(x_blob).float()
y_blob = torch.from_numpy(y_blob).long()

x_train, x_test, y_train, y_test = train_test_split(x_blob, y_blob, test_size=0.2, random_state=RANDOM_SEED)

class BlobModel(nn.Module):
    def __init__(self, input_features, output_features, hidden_units=8):
        super().__init__()
        self.linear_layer_stack = nn.Sequential(
                nn.Linear(in_features=input_features, out_features=hidden_units),
                nn.Linear(in_features=hidden_units, out_features=hidden_units),
                nn.Linear(in_features=hidden_units, out_features=output_features)
        )

    def forward(self, x):
        return self.linear_layer_stack(x)

model_4 = BlobModel(input_features=2, output_features=4)

