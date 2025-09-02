import numpy as np


A = np.array([[25, 2], [5, 4]])

print(25+4)
print(np.trace(A))

#The trace operator has a number of useful properties that come in handy while rearranging linear algebra equations, e.g.:
# - Tr(A) = Tr(Aᵀ)
# - Assuming the matrix shapes line up: Tr(ABC) = Tr(CAB) = Tr(BCA)

#In particular, the trace operator can provide a convenient way to calculate a matrix's Frobenius norm:
# ‖A‖_F = √(Tr(AAᵀ))