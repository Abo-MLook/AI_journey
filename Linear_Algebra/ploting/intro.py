import numpy as np
import matplotlib.pyplot as plt

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


def plot_lines(A_system, axis_range=(-4, 4)):
    """
    Plot 2D linear equations given an augmented matrix [A | b].
    Works for any 2x2 system.

    Parameters:
        A_system: numpy array shape (2, 3)
                  augmented matrix [A | b]
        axis_range: tuple (min, max) for both x and y axes
    """
    A = A_system[:, :-1]  # coefficients
    b = A_system[:, -1]  # constants

    # Generate x values
    x_vals = np.linspace(axis_range[0], axis_range[1], 200)

    # Plot each line
    for i in range(A.shape[0]):
        a1, a2 = A[i]
        c = b[i]

        if a2 != 0:  # Normal case: solve for y
            y_vals = (c - a1 * x_vals) / a2
            plt.plot(x_vals, y_vals, label=f"Eq {i + 1}: {a1}x + {a2}y = {c}")
        else:  # Vertical line (if coefficient of y = 0)
            x_const = c / a1
            plt.axvline(x_const, label=f"Eq {i + 1}: x = {x_const}")

    # Format axes
    plt.axhline(0, color='black', linewidth=0.7)
    plt.axvline(0, color='black', linewidth=0.7)
    plt.xlim(axis_range)
    plt.ylim(axis_range)
    plt.xticks(range(axis_range[0], axis_range[1] + 1))
    plt.yticks(range(axis_range[0], axis_range[1] + 1))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("System of Linear Equations")
    plt.show()
plot_lines(A_system,(-10,10))
