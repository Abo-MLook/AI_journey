import numpy as np

zeroM = np.zeros((2,3),"int32")
print(zeroM)

onesM = np.ones((zeroM.shape),"float16")
print(onesM)
print()

# mat with filling num
mat_7 = np.full((3,2,3),7)
print(mat_7)
print()

# mat with random nums
mat_rand = np.random.randint(1,11,(onesM.shape))
print(f"random:\n{mat_rand}")
print()

# identity mat
mat_Id = np.identity(3,"int")
print(f"Identity mat is :\n{mat_Id}")
print()

# repeat mat
mat1 = np.array([[1,2,3]])
mat2 = np.repeat(mat1,3,axis=0)
print(f"mat repeated : \n{mat2}")
print()
