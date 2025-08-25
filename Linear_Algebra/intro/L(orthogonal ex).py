import numpy as np

I3 = np.identity(3,int)
print(I3)

c1 = I3[:,0]
c2 = I3[:,1]
c3 = I3[:,2]

print()
print("c1 dot c2 = ",np.dot(c1,c2))
print("c1 dot c3 = ",np.dot(c1,c3))
print("c2 dot c3 = ",np.dot(c2,c3))
print()

print("c1 unit form : ",np.linalg.norm(c1))
print("c2 unit form : ",np.linalg.norm(c2))
print("c3 unit form : ",np.linalg.norm(c3))
print()
print()



K = np.array([[2/3,-2/3,1/3],[1/3,2/3,2/3],[2/3,1/3,-2/3]])
print(K)

c1 = K[:,0]
c2 = K[:,1]
c3 = K[:,2]

print()
print("c1 dot c2 =", abs(round(np.dot(c1,c2), 12)))
print("c1 dot c3 =", round(np.dot(c1,c3), 12))
print("c2 dot c3 =", abs(round(np.dot(c2,c3), 12)))
print()
print("c1 norm =", round(np.linalg.norm(c1), 12))
print("c2 norm =", round(np.linalg.norm(c2), 12))
print("c3 norm =", round(np.linalg.norm(c3), 12))