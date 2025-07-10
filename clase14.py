import numpy as np

np.set_printoptions(suppress=True)  # Suppress scientific notation for small numbers
A = np.array([[3, 1], [2, 1]])
print("Matrix A:\n", A)

# Solve the linear equation Ax = B
# where B is a vector
B = np.array([[1], [1]])
A_inv = np.linalg.inv(A)
print("Inverse of Matrix A:\n", A_inv)

# Calculate the solution x
x = A_inv.dot(B)
print("Solution x:\n", x)
print(A.dot(x))  # Should return B

# Now let's solve another equation Ax = C
sol_2 = A_inv.dot(np.array([[3], [7]]))
print("Solution for Ax = [3, 7]:\n", sol_2)
print(A.dot(sol_2))  # Should return [3, 7]