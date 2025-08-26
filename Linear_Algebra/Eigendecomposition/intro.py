import numpy as np

# This was used earlier as a matrix X; it has nice clean integer eigenvalues...
A = np.array([[4, 2], [-5, -3]])
lambdas, V = np.linalg.eig(A)
print(V)
print()

print(lambdas)
print()

Vinv = np.linalg.inv(V)
print(Vinv)
print()

Lambda = np.diag(lambdas)
print(Lambda)
print()

print(np.dot(V, np.dot(Lambda, Vinv)))