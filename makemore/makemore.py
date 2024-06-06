
# Makemore implementation

import torch 
import torch.nn as nn
import matplotlib.pyplot as plt

# read all the names
words = open("names.txt", 'r').readlines()

# build a list of characters used
chars = sorted(list(set(''.join(words))))

# create mappings of characters to/from integers
char_to_int = {c:i+1 for i,c in enumerate(chars)}
char_to_int['.'] = 0
int_to_char = {i:c for c,i in char_to_int.items()}

# build the dataset
block_size = 3

def build_dataset(words):
    X, Y = [], []

    for word in words:
        context[0] = block_size
        for char in word + '.':
            idx = char_to_int[char]
            X.append[context]
            Y.append[idx]
            context = context[1:] + [idx]

    X = torch.tensor(X)
    Y = torch.tensor(Y)
    print(X.shape, Y.shape)
    return X, Y

