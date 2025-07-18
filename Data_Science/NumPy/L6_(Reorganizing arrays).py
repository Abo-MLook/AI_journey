import numpy as np

#========================== reshape and resize
print("reshape :")
before = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) # this is 4 X 4 mat
print(before)
print()

after = before.reshape((6,2)) # this is 6 X 2 mat          but error when not match of total size
print(after)
print()

print("resize :")
before1 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # this is 3 X 3 mat
after = np.resize(before1,(4,2)) # this is 4 X 2 mat , but no error when not match of total size
print(after)
print()
#----- exit


#========================== Vertically stacking vectors
print("V stacking :")
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(f"v1 = {v1}")
print(f"v2 = {v2}")
v3 = np.vstack([v1,v2,v1,v2])
print(f"v3 = \n{v3}")
print()
#----- exit

#========================== Vertically stacking vectors
print("V stacking :")
v1 = np.array([[1,2,3],[8,9,10]])
v2 = np.array([[5,6,7],[11,12,13]])
print(f"v1 = \n{v1}")
print(f"v2 = \n{v2}")
v3 = np.hstack([v1,v2])
print(f"v3 = \n{v3}")
print()
#----- exit