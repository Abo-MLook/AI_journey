import numpy as np

A = np.array([[2, 1], [1, 2]])

lambdas, Q = np.linalg.eig(A)

Lambda = np.diag(lambdas)

print(np.dot(Q, np.dot(Lambda, Q.T)))

print()

#(As a quick aside, we can demonstrate that Q is an orthogonal matrix because QᵀQ = QQᵀ = I.) :

print(np.dot(Q.T, Q))

print()

print(np.dot(Q, Q.T))