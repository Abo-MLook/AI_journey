from Linear_Algebra.Youtube_course.Affine_Transformation.L_Affine_Transformation import plot_vectors
import numpy as np
import matplotlib.pyplot as plt
I = np.identity(2)

# function to convert column of matrix to 1D vector:
def vectorfy(mtrx, clmn):
    return np.array(mtrx[:,clmn]).reshape(-1)

B = np.array([[1, 0], [0, 1]])
J = np.array([[-0.5, 0], [0, 2]])

print(abs(np.linalg.det(J)))

lambdas, V = np.linalg.eig(J)
print(f"EigenValues I2 : \n{lambdas}")

JB = np.dot(J, B)
plot_vectors([vectorfy(B, 0), vectorfy(B, 1), vectorfy(JB, 0), vectorfy(JB, 1)],
            ['lightblue', 'lightgreen', 'blue', 'green'])
plt.xlim(-1, 3)
_ = plt.ylim(-1, 3)
plt.show()

#======================================================
# Finally, let's apply the matrix D  which scales vectors by doubling along both the c and y axes:
D = I*2
print(abs(np.linalg.det(D)))
DB = np.dot(D, B)
plot_vectors([vectorfy(B, 0), vectorfy(B, 1), vectorfy(DB, 0), vectorfy(DB, 1)],
            ['lightblue', 'lightgreen', 'blue', 'green'])
plt.xlim(-1, 3)
_ = plt.ylim(-1, 3)
plt.show()
