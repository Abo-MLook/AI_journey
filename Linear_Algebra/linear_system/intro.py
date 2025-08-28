import numpy as np
import matplotlib.pyplot as plt
from Linear_Algebra.ploting.intro import plot_lines



A = np.array([
        [-1, 3],
        [3, 2]
    ], dtype=np.dtype(float))

b = np.array([7, 1], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

print(f"Shape of A: {A.shape}")
print(f"Shape of b: {b.shape}")

# print(f"Shape of A: {np.shape(A)}")
# print(f"Shape of A: {np.shape(b)}")


x = np.linalg.solve(A, b)

print(f"Solution: {x}")



d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")


#2 - Visualizing 2x2 Systems as Plotlines
print()
A_system = np.hstack((A, b.reshape((2, 1))))
print(A_system)
