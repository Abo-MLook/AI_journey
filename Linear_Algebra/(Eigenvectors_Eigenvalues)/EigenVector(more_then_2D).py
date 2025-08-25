from Linear_Algebra.Affine_Transformation.L_Affine_Transformation import plot_vectors
import numpy as np
import matplotlib.pyplot as plt

# While plotting gets trickier in higher-dimensional spaces, we can nevertheless find and use eigenvectors with more than two dimensions.
# Here's a 3D example (there are three dimensions handled over three rows):

X = np.array([[25, 2, 9], [5, 26, -5], [3, 7, -1]])

lambdas_X, V_X = np.linalg.eig(X)

print(V_X)
print()
print(lambdas_X)
print()
print()

#(Xv = λv)
v_X = V_X[:,0]
lambda_X = lambdas_X[0]
print(np.dot(X, v_X)) # matrix multiplication Xv
print()

print(lambda_X * v_X) # matrix multiplication λv