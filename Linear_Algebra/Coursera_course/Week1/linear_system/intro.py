import numpy as np
from Linear_Algebra.Coursera_course.Week1.ploting.intro import plot_lines



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

# another way
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
plot_lines(A_system,(-10,10))



#3 - System of Linear Equations with No Solutions


A_2 = np.array([
        [-1, 3],
        [3, -9]
    ], dtype=np.dtype(float))

b_2 = np.array([7, 1], dtype=np.dtype(float))

d_2 = np.linalg.det(A_2)

print(f"Determinant of matrix A_2: {d_2:.2f}")
try:
    x_2 = np.linalg.solve(A_2, b_2)
except np.linalg.LinAlgError as err:
    print(err)

A_2_system = np.hstack((A_2, b_2.reshape((2, 1))))
print(A_2_system)
plot_lines(A_2_system)

# 4 - System of Linear Equations with an Infinite Number of Solutions
b_3 = np.array([7, -21], dtype=np.dtype(float))
A_3_system = np.hstack((A_2, b_3.reshape((2, 1))))
try:
    x_2 = np.linalg.solve(A_2, b_3)
except np.linalg.LinAlgError as err:
    print(err)
print(A_3_system)
plot_lines(A_3_system)
