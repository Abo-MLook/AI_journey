from Linear_Algebra.Affine_Transformation.L_Affine_Transformation import plot_vectors
import numpy as np
import matplotlib.pyplot as plt



A = np.array([[-1, 4], [2, -2]])

lambdas, V = np.linalg.eig(A)

print(V)
print()
print(lambdas)

#Let's confirm that ( Av = λv ) for the first eigenvector:
v1 = V[:,0]
lambdas1 = lambdas[0]
print()
print()

Av = np.dot(A,v1) # Av
print(Av)

print()

Lv = lambdas1 * v1 # λv
print(Lv)

print(f"Av is == λv ? : {Av==Lv}")


plot_vectors([Av, v1], ['blue', 'lightblue'])
plt.xlim(-1, 2)
_ = plt.ylim(-1, 2)
plt.show()
