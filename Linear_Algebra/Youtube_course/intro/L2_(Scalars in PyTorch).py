import torch
# Scalars in PyTorch
# PyTorch tensors are designed to be pythonic, i.e., to feel and behave like NumPy arrays , it is fun and flixable
# The advantage of PyTorch tensors relative to NumPy arrays is that they easily be used for operations on GPU and ML
# more on : https://docs.pytorch.org/docs/stable/tensors.html

x = 25
x_pt = torch.tensor(25) # type specification optional, e.g.: dtype=torch.float16
print(x_pt.shape) # because it is scalser there is no dimtinosions