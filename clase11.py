import numpy as np

A = np.array([[2, 3], [5, 7], [11, 13]])
B = np.array([[1, 3], [2, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

AB_t = A.dot(B).T
B_tA_t = B.T.dot(A.T)
print(AB_t == B_tA_t)
