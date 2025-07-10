# Create a virtual environment with the command:
# python -m venv env
# Activate the virtual environment with the command:
# env\Scripts\activate
# And install the required packages

import numpy as np

escalar = 5.679
vector = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
tensor = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
])

print("Escalar:", escalar)
print("Escalar shape doesn't exist")
print("Vector shape:", vector.shape) # returns the shape of the vector like (3,) or (3,1)
print("vector:", vector)
print("Vector length:", len(vector)) # returns the length of the elements in the first dimension
print("matrix shape:", matrix.shape) # returns the shape of the matrix like (2,2) or (2,2,1)
print("matrix size:", matrix.size) # returns the number of elements in the matrix
print("matrix:\n", matrix)
print("tensor shape:", tensor.shape) # returns the shape of the tensor like (3,3,3).
# The first number is the number of rows, the second number is the number of columns and the third number is the number of the structure repeated
