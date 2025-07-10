import numpy as np

A = np.array([[2, 3], [5, 7], [11, 13]])
B = np.array([[1, 3], [2, 1]])
C = np.array([[3, 1], [4, 2]])

# Asociative property
ABC = A.dot(B.dot(C))
print("A dot (B dot C):\n", ABC)

AB_C = A.dot(B).dot(C)
print("A dot B dot C:\n", AB_C)

print(ABC == AB_C)

# Distributive property
D = A.dot(B + C)
print("A dot (B + C):\n", D)

E = A.dot(B) + A.dot(C)
print("A dot B + A dot C:\n", E)

print(D == E)

# Commutative property
v1 = np.array([[2], [7]])
v2 = np.array([[3], [5]])

v1_tv2 = v1.T.dot(v2)
v2_tv1 = v2.T.dot(v1)
print("v1.T dot v2:\n", v1_tv2)
print("v2.T dot v1:\n", v2_tv1)