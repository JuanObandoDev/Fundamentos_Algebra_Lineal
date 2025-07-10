import numpy as np

escalar = 5.679
vector = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
tensor = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
])

# Transpose operations
print("Escalar doesn't have a transpose")
vector_t = vector.T # .T is used to transpose arrays and matrices
print("Vector:\n", vector)
print("Vector tranpose:\n", vector_t)

matrix_t = matrix.T
print("Matrix:\n", matrix)
print("Matrix transpose:\n", matrix_t)

tensor_t = tensor.T
print("Tensor:\n", tensor)
print("Tensor transpose:\n", tensor_t)

# Matrix addition
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[6, 5], [4, 3], [2, 1]])
C = A + B
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix C (A + B):\n", C)

# Matrix plus escalar
D = matrix + escalar
print("Escalar:", escalar)
print("Matrix:\n", matrix)
print("Matrix D (matrix + escalar):\n", D)

# Exercise: Create a matrix 5*5 and add with his transpose
matrix_5x5 = np.random.randint(1, 10, (5, 5)) 
print("Matrix 5x5:\n", matrix_5x5)
matrix_5x5_t = matrix_5x5.T
print("Matrix 5x5 transpose:\n", matrix_5x5_t)
matrix_5x5_sum = matrix_5x5 + matrix_5x5_t
print("Sum of Matrix 5x5 and its transpose:\n", matrix_5x5_sum)