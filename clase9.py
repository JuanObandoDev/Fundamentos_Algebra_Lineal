import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
B = np.array([[2, 3], [5, 7], [11, 13]])

print("Matrix A shape:\n", A.shape)
print("Matrix B shape:\n", B.shape)

# internal product between two matrices
C = A.dot(B)
try:
    D = B.dot(A) # This will raise an error because the shapes are not compatible (3, 2) and (4, 3)
except ValueError as e:
    pass
