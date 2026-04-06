from L_Affine_Transformation import plot_vectors
import numpy as np
import matplotlib.pyplot as plt

v = np.array([3, 1])
A = np.array([[-1, 4], [2, -2]])
Av = np.dot(A, v)
print(Av)
plot_vectors([v, Av], ['lightblue', 'blue'])
plt.xlim(-1, 5)
_ = plt.ylim(-1, 5)

plt.show()


v2 = np.array([2, 1])
plot_vectors([v2, np.dot(A, v2)], ['lightgreen', 'green'])
plt.xlim(-1, 5)
_ = plt.ylim(-1, 5)
plt.show()