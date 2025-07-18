import numpy as np
#-------------

zeroM = np.zeros((2,3),"int32")
print(zeroM)

onesM = np.ones((zeroM.shape),"float16")
print(onesM)
print()
#-------------

# mat with filling num
mat_7 = np.full((3,2,3),7)
print(mat_7)
print()
#-------------

# mat with random nums
mat_rand = np.random.randint(1,11,(onesM.shape))
print(f"random:\n{mat_rand}")
print()
#-------------

# identity mat
mat_Id = np.identity(3,"int")
print(f"Identity mat is :\n{mat_Id}")
print()
#-------------

# repeat mat or array
mat1 = np.array([[1,2,3]])
mat2 = np.repeat(mat1,3,axis=0)
print(f"mat repeated : \n{mat2}")
print()

#-------------
#exercise :
#1  1  1  1  1
#1  0  0  0  1
#1  0  9  0  1
#1  0  0  0  1
#1  1  1  1  1
print("\n first way :")
exercise = np.zeros((5,5),int)
print(exercise)
print()
exercise[0,:] = 1
exercise[-1,:] = 1
exercise[:,0] = 1
exercise[:,-1] = 1
exercise[2,2] = 9
print(exercise)

print("\n second way better one :")
exercise = np.ones((5,5),int)
exerciseZ = np.zeros((3,3),int)
exerciseZ[1,1] = 9
print(exercise)
print(f"\n{exerciseZ}")

exercise[1:4,1:4] = exerciseZ
print(f"\n:{exercise}")


# 🔗 Array Creation Routines: https://numpy.org/doc/stable/reference/routines.array-creation.html