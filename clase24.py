import numpy as np

# This code demonstrates the creation of a diagonal matrix from a vector and performs some operations on it.
vector = np.array([1, 2, 3, 4, 5])
matrix = np.diag(vector)
print("Vector:", vector)
print("Matrix:\n", matrix)

# Creating a diagonal matrix but not square
print("Submatrix:\n", matrix[0:4, 0:3])
print("Submatrix:\n", matrix[0:3, 0:4])

# Pondering the dot product of a matrix with a vector
A = np.diag([2, 3, 4, 5])
print("Matrix A:\n", A)
v1 = np.array([[1, 1, 1, 1]])
print("Vector v1:\n", v1)
print("Dot product:\n", A.dot(v1.T))

# Calculating the inverse of a diagonal matrix
A_inv = np.diag([1/2, 1/3, 1/4, 1/5])
print("Inverse of A:\n", A_inv)
print("Dot product of A and its inverse:\n", A.dot(A_inv))

A_inv_calc = np.linalg.inv(A)
print("Calculated inverse of A:\n", A_inv_calc)
print("Dot product of A and its calculated inverse:\n", A.dot(A_inv_calc))

# Symmetric matrix example
print("Transpose of A:\n", A.T)
print("A matrix is symmetric:", A)

# Not only diagonal matrices are symmetric
symmetric = np.array([
    [1, 2, 3],
    [2, -1, 7],
    [3, 7, 11]
])
print("Symmetric matrix:\n", symmetric)
print("Transpose of symmetric matrix:\n", symmetric.T)