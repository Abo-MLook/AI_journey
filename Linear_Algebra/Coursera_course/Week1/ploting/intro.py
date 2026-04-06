import numpy as np
import matplotlib.pyplot as plt



def plot_lines(A_system, axis_range=(-10, 10)):
    """
    Plot 2D linear equations given an augmented matrix [A | b].
    Works for any 2x2 system.
    """
    A = A_system[:, :-1]  # coefficients
    b = A_system[:, -1]   # constants

    # Make figure larger
    plt.figure(figsize=(8, 8))  # (width, height) in inches

    # Generate x values
    x_vals = np.linspace(axis_range[0], axis_range[1], 400)

    # Plot each line
    for i in range(A.shape[0]):
        a1, a2 = A[i]
        c = b[i]

        if a2 != 0:  # Normal line
            y_vals = (c - a1 * x_vals) / a2
            plt.plot(x_vals, y_vals, label=f"Eq {i+1}: {a1:.1f}x + {a2:.1f}y = {c:.1f}")
        else:  # Vertical line
            x_const = c / a1
            plt.axvline(x_const, label=f"Eq {i+1}: x = {x_const:.1f}")

    # Axes formatting
    plt.axhline(0, color='black', linewidth=0.7)
    plt.axvline(0, color='black', linewidth=0.7)
    plt.xlim(axis_range)
    plt.ylim(axis_range)
    plt.xticks(range(axis_range[0], axis_range[1] + 1))
    plt.yticks(range(axis_range[0], axis_range[1] + 1))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=10)
    plt.xlabel("x1", fontsize=12)
    plt.ylabel("x2", fontsize=12)
    plt.title("System of Linear Equations", fontsize=14)
    plt.show()
