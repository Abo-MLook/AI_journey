import numpy as np



X = np.array([[1, 2, 4], [2, -1, 3], [0, 5, 1]])
lambdas, V = np.linalg.eig(X)

print(f"The sum products of all Eigenvalues of these :\n{lambdas}")
SP = np.prod(lambdas)
print()

print(f"sum products of all Eigenvalues = {SP}")


detX = np.linalg.det(X)
print(f"the determinant of X = {detX}")