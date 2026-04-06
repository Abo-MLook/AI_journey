from L_Affine_Transformation import plot_vectors
import numpy as np
import matplotlib.pyplot as plt

#We can concatenate several vectors together into a matrix (say,V),
#where each column is a separate vector. Then, whatever linear transformations we apply to V
# will be independently applied to each column (vector):

v = np.array([3, 1])
print(v)
# recall that we need to convert array to 2D to transpose into column, e.g.:
#v = np.matrix(v).T
#print(v)

v2 = np.array([2, 1])
v3 = np.array([-3, -1]) # mirror image of v over both axes
v4 = np.array([-1, 1])

V = np.concatenate((np.matrix(v).T, np.matrix(v2).T,np.matrix(v3).T,np.matrix(v4).T), axis=1)
print(V)

I = np.array([[1, 0], [0, 1]])
A = np.array([[-1, 4], [2, -2]])
print()
IV = np.dot(I, V)
print(IV)
print()

AV = np.dot(A, V)
print(AV)
print()

# function to convert column of matrix to 1D vector:
def vectorfy(mtrx, clmn):
    return np.array(mtrx[:,clmn]).reshape(-1)


print(vectorfy(V, 0))
print(vectorfy(V, 0) == v)


plot_vectors([vectorfy(V, 0), vectorfy(V, 1), vectorfy(V, 2), vectorfy(V, 3),
             vectorfy(AV, 0), vectorfy(AV, 1), vectorfy(AV, 2), vectorfy(AV, 3)],
            ['lightblue', 'lightgreen', 'lightgray', 'orange',
             'blue', 'green', 'gray', 'red'])
plt.xlim(-4, 6)
_ = plt.ylim(-5, 5)


plt.show()