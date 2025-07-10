import numpy as np

vector = np.array([3, 4, 5])
matrix = np.array([[1, 2], [3, 4], [5, 6]])

# This cannot be done as vector and matrix have different shapes
try:
    A = vector + matrix
except ValueError as e:
    pass

# This can be done as matrix and vector have compatible shapes with broadcasting
A = matrix.T + vector
print("Matrix transpose:\n", matrix.T)
print("Vector:\n", vector)
print("Result of matrix transpose + vector:\n", A)

# Exercise: Create a matrix 5*5 and add with vector of shape (5,)
matrix_5x5 = np.random.randint(1, 10, (5, 5))
vector_5 = np.random.randint(1, 10, 5)
print("Matrix 5x5:\n", matrix_5x5)
print("Vector 5:\n", vector_5)
matrix_5x5_sum = matrix_5x5 + vector_5
print("Sum of Matrix 5x5 and Vector 5:\n", matrix_5x5_sum)
