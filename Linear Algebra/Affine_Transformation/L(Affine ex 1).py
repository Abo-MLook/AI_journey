from L_Affine_Transformation import plot_vectors
import numpy as np
import matplotlib.pyplot as plt


v = np.array([3, 1])
E = np.array([[1,0],[0,-1]])

Ev = np.dot(E, v)
plot_vectors([v, Ev], ['lightblue', 'blue'])
plt.xlim(-1, 5)
_ = plt.ylim(-3, 3)
plt.show()