import numpy as np

# -------------------------------------========= Matrices

#=====  mult
a = np.ones((2,3))
print(a)

b = np.full((3,2),2)
print(b)
print()

print(np.matmul(a,b))
print()
#----

#=====  Find the determinant

d = np.identity(3)
print(d)
print(f"The deteminant is : {np.linalg.det(d)}")
print()
#----

#=====  Transposed
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat)
print(mat.T)
print()
#----

#=====  inverse
mat = np.array([[1, 2, 3], [4, 5, 6],[1, 8, 9]])
print(mat)
print(f"The inverse is :\n{np.linalg.inv(mat)}")
print()
#----

# more  🔗 Linear Algebra Docs: https://numpy.org/doc/stable/reference/routines.linalg.html