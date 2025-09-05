import numpy as np

# 1.2 - Solving Systems of Linear Equations using Matrices :

A = np.array([
        [4, -3, 1],
        [2, 1, 3],
        [-1, 2, -5]
    ], dtype=np.dtype(float))

b = np.array([-10, 0, 17], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print()
print("\nArray b:")
print(b)
print()


print(f"Shape of A: {np.shape(A)}")
print(f"Shape of b: {np.shape(b)}")
print()



x = np.linalg.solve(A, b)

print(f"Solution: {x}")
print()

#========================================================

# 1.3 - Evaluating the Determinant of a Matrix
d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")
#========================================================

# 1.4 - What happens if the system has no unique solution?
A_2= np.array([
        [1, 1, 1],
        [0, 1, -3],
        [2, 1, 5]
    ], dtype=np.dtype(float))

b_2 = np.array([2, 1, 0], dtype=np.dtype(float))
# will produce an error because it is singluar det is = 0
print(np.linalg.solve(A_2, b_2))
print()

d_2 = np.linalg.det(A_2)

print(f"Determinant of matrix A_2: {d_2:.2f}")