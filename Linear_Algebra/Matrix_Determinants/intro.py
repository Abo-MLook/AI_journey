import numpy as np
import torch

X = np.array([[4, 2], [-5, -3]])

detX = np.linalg.det(X)
print(f"determinant = {detX}\n")

N = np.array([[-4, 1], [-8, 2]])
detN = np.linalg.det(N)
print(f"determinant = {detN}\n")


# Uncommenting the following line results in a "singular matrix" error
# Ninv = np.linalg.inv(N)

# in pyTorch
N = torch.tensor([[-4, 1], [-8, 2.]]) # must use float not int
detNt = torch.det(N)
print(f"determinant = {detNt}")