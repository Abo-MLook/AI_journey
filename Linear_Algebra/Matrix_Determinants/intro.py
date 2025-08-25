import numpy as np

X = np.array([[4, 2], [-5, -3]])

detX = np.linalg.det(X)
print(f"determinant = {detX}\n")

N = np.array([[-4, 1], [-8, 2]])
detN = np.linalg.det(N)
print(f"determinant = {detN}\n")
