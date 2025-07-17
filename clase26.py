import numpy as np

# Orthogonal matrix
matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
print("Matrix:\n", matrix)
# Prove that the matrix is orthogonal
print(matrix[:, 0].dot(matrix[:, 1]))
print(matrix[:, 0].dot(matrix[:, 2]))
print(matrix[:, 1].dot(matrix[:, 2]))
print(np.linalg.norm(matrix[:, 0]))
print(np.linalg.norm(matrix[:, 1]))
print(np.linalg.norm(matrix[:, 2]))
print(matrix[0, :].dot(matrix[1, :]))
print(matrix[0, :].dot(matrix[2, :]))
print(matrix[1, :].dot(matrix[2, :]))
print(np.linalg.norm(matrix[0, :]))
print(np.linalg.norm(matrix[1, :]))
print(np.linalg.norm(matrix[2, :]))

# Rotation matrix
A = np.array([
    [np.cos(100), -np.sin(100)],
    [np.sin(100), np.cos(100)]
])
print("Rotation Matrix A:\n", A)
print(np.linalg.norm(A[0, :]))
print(np.linalg.norm(A[1, :]))
print(np.linalg.norm(A[:, 0]))
print(np.linalg.norm(A[:, 1]))
print(A[0, :].dot(A[1, :]))
print(A[:, 0].dot(A[:, 1]))
A_t = A.T
print(A_t.dot(A))
print(A.dot(A_t))