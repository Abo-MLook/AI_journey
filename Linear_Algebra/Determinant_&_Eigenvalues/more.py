from Linear_Algebra.Affine_Transformation.L_Affine_Transformation import plot_vectors
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

N = np.array([[-4, 1], [-8, 2]])
detN = np.linalg.det(N)

NB = np.dot(N, B)
print(NB)