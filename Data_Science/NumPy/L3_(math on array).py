import numpy as np


#========================== coping
# be careful when coping

a = np.array([1,2,3])
b = a
b[0] = 99
print(b)
print(a) # changed because b was pointing to a   (pointer)

a = np.array([1,2,3])
b = a.copy() # this is real coping not pointing
b[0] = 99
print(b)
print(a)
print("copy finish---")
print()
#----- exit

#========================== math

a = np.array([1,2,3])
a = a**2
print(a)
a = a - (a - 1)
print(a)
b = np.ones(a.shape,int)
a +=b
print(a)
# and so on ....
print("math finish---")
print()
#----- exit


#-----🔗 Math Routines Docs: https://numpy.org/doc/stable/reference/routines.math.html

