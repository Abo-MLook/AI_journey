import numpy as np

A = np.array([[-1, 2], [3, -2], [5, 7]])
U, d, VT = np.linalg.svd(A) # V is already transposed

print(U)
print()
print(d)
print()
print(VT)
print()

print(np.diag(d))
print()
D = np.concatenate((np.diag(d), [[0, 0]]), axis=0)
print(D)
print()
print(np.dot(U, np.dot(D, VT)))