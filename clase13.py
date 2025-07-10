import numpy as np

identity = np.eye(4)  # Create a 4x4 identity matrix
print("Identity Matrix:\n", identity)

# Create a vector and multiply it with the identity matrix
vector = np.array([[2], [3], [5], [7]])
print(identity.dot(vector))
print("Vector:\n", vector)

# Create a matrix and do his inverse, also multiply matrix with its inverse and returns identity matrix
A = np.array([[1, 0, 1], [0, 1, 1], [-1, 1, 1]])
print("Matrix A:\n", A)
inverse_A = np.linalg.inv(A)
print("Inverse of Matrix A:\n", inverse_A)
print("A dot Inverse of A:\n", A.dot(inverse_A))