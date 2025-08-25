import numpy as np

def inversable(mat):
    det = np.linalg.det(mat)
    if det > 0 :
        return "has an inverse\n"
    else:
        return "it is singular\n"




mat1 = np.array([[25,2],[3,4]])
mat2 = np.array([[-2,0],[0,-2]])
mat3 = np.array([[2,1,-3],[4,-5,2],[0,-1,3]])

inversable(mat1)
inversable(mat2)
inversable(mat3)