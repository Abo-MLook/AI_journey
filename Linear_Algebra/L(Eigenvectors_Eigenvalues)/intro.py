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


# And again for the second eigenvector of A:


v2 = V[:,1]
lambdas2 = lambdas[1]
print()
print()

Av2 = np.dot(A,v2) # Av
print(Av2)

print()

Lv = lambdas2 * v2 # λv
print(Lv)

print(f"Av is == λv ? : {Av2==Lv}")


plot_vectors([Av, v1, Av2, v2],
            ['blue', 'lightblue', 'green', 'lightgreen'])
plt.xlim(-1, 4)
_ = plt.ylim(-3, 2)
plt.show()