import numpy as np

vector = np.array([1, 2, 0, 5, 6, 0])
print(np.linalg.norm(vector, ord=0))  # Count non-zero elements

vector = np.array([1, -1, 1, -1, 1])
print(np.linalg.norm(vector, ord=1))  # Sum of absolute values

vector = np.array([1, 1])
print(np.linalg.norm(vector)) # Euclidean norm (default, ord=2)
print(np.linalg.norm(vector, ord=2))  # Explicitly using ord=2

vector = np.array([1, 2, 3, 4, 5, 6])
print(vector)
print(np.linalg.norm(vector, ord=2)**2) # Squared Euclidean norm
print(vector.T.dot(vector))  # Dot product with itself

vector = np.array([1, 2, 3, -100])
print(np.linalg.norm(vector, ord=np.inf))  # Maximum absolute value