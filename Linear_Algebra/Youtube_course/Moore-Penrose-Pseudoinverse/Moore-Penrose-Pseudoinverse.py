import numpy as np



#Let’s calculate the pseudoinverse 𝐴+ of some matrix A using the formula from the slides:
# A+ =VD+U^T

A = np.array([[-1,2],[3,-2],[5,7]])
#print(f"DET = {np.linalg.det(A)}") error not sequre so detirmenant not exist

U, d, VT = np.linalg.svd(A)

#To create D+, we first invert the non-zero values of D:
D = np.diag(d)
#1/8.669
#1/4.104
Dinv = np.linalg.inv(D)


#D+ must have the same dimensions as A^T in order for VD+U^T matrix multiplication to be possible:
Dplus = np.concatenate((Dinv, np.array([[0, 0]]).T), axis=1)

# final result
print(np.dot(VT.T, np.dot(Dplus, U.T)))
print()

#Working out this derivation is helpful for understanding how Moore-Penrose pseudoinverses work,
# but unsurprisingly NumPy is loaded with an existing method pinv():

print(np.linalg.pinv(A))