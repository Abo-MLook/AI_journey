from Linear_Algebra.Youtube_course.Affine_Transformation.L_Affine_Transformation import plot_vectors
import numpy as np
import matplotlib.pyplot as plt

# function to convert column of matrix to 1D vector:
def vectorfy(mtrx, clmn):
    return np.array(mtrx[:,clmn]).reshape(-1)



B = np.array([[1, 0], [0, 1]])
plot_vectors([vectorfy(B, 0), vectorfy(B, 1)],
            ['lightblue', 'lightgreen'])
plt.xlim(-1, 3)
_ = plt.ylim(-1, 3)
plt.show()

#======================================================
# det = 0  ,, No Volume
B = np.array([[1, 0], [0, 1]])
N = np.array([[-4, 1], [-8, 2]])
detN = np.linalg.det(N)
print(f"det = {detN}")
NB = np.dot(N, B)
print(NB)


plot_vectors([vectorfy(B, 0), vectorfy(B, 1), vectorfy(NB, 0), vectorfy(NB, 1)],
            ['lightblue', 'lightgreen', 'blue', 'green'])
plt.xlim(-6, 6)
_ = plt.ylim(-9, 3)
plt.show()
lambdas, V = np.linalg.eig(N)
print(f"EigenValues : \n{lambdas}")
# Aha! If any one of a matrix's eigenvalues is zero, then the product of the eigenvalues must
# be zero and the determinant must also be zero.

print()
print()

#======================================================
# det = 1  ,,  Volume same
I = np.identity(2)
print(f"det I2 = {np.linalg.det(I)}")
lambdas, V = np.linalg.eig(I)
print(f"EigenValues I2 : \n{lambdas}")

IB = np.dot(I, B)
print()
print(IB)
plot_vectors([vectorfy(B, 0), vectorfy(B, 1), vectorfy(IB, 0), vectorfy(IB, 1)],
            ['lightblue', 'lightgreen', 'blue', 'green'])
plt.xlim(-1, 3)
_ = plt.ylim(-1, 3)
plt.show()

