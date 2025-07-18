import numpy as np

A = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
])

lambdas, vectors = np.linalg.eig(A.T)
print("Eigenvalues:", lambdas)
print("Eigenvectors:\n", vectors)
print(A[lambdas == 0, :])