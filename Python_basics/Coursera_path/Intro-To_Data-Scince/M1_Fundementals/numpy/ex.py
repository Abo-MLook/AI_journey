import numpy as  np


x = np.random.rand(3, 4, 5)
print(x)


print()

x = x.reshape(-1, 1)
print(x)
print()
print()


x = np.random.rand(1, 4, 5, 1, 2)
print(x)
print()
print()
x = np.squeeze(x)
print(x)
print()



arr = np.array([[1, 2, 3], [4, 5, 6]])
flattened = arr.flatten()
print(flattened)
print(flattened.shape)

print()
arr = np.array([1, 2, 3])

# Add a new axis to make it a column vector (2D array)
column_vector = arr[:, np.newaxis]
print(column_vector)

print()
arr = np.array([1, 2, 3, 4])
resized = np.resize(arr, (2, 6))
print(resized)
