import numpy
import numpy as np

stats = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(stats)
print(f"")

print(f"min is : {np.min(stats)}")
print(f"max is : {np.max(stats)}")

print()

print(f"min on each row is : {np.min(stats,axis=1)}")
print(f"min on each column is : {np.min(stats,axis=0)}")
print(f"max on each row is : {np.max(stats,axis=1)}")
print(f"max on each column is : {np.max(stats,axis=0)}")
print()