import numpy as np

vector = np.array([2, 3])
matrix = np.array([[1, 2], [3, 4], [5, 6]])

# Matrix multiplication
A = matrix * vector
print("Result of matrix * vector:\n", A)

# Internal product
B = matrix.dot(vector)
print("Result of matrix dot vector:\n", B)

# Internal product can be done also with:
C = np.dot(matrix, vector)
print("Result of np.dot(matrix, vector):\n", C)

# Exercise: Multiply a matrix with a vector and then multiply a vector with a matrix
matrix_A = np.random.randint(1, 10, (2, 2))
vector_A = np.random.randint(1, 10, 2)
result_A = matrix_A * vector_A
result_B = vector_A * matrix_A
print("Matrix A:\n", matrix_A)
print("Vector A:\n", vector_A)
print("Result of Matrix A * Vector A:\n", result_A)
