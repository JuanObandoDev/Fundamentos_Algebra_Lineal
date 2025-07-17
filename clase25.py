import numpy as np
import matplotlib.pyplot as plt

# Orthogonal vectors, orthogonal means that the angle between them is 90 degrees.
x = np.array([0, 0, 2, 2])
y = np.array([0, 0, 2, -2])

plt.quiver(
    [x[0], y[0]],
    [x[1], y[1]],
    [x[2], y[2]],
    [x[3], y[3]],
    angles='xy', scale_units='xy', scale=1
)
plt.xlim(-2, 4)
plt.ylim(-3, 3)
plt.show()

v1 = np.array([[2, 2]])
v2 = np.array([[2, -2]])
print("Vector v1:", v1)
print("Vector v2:", v2)
print("Dot product of v1 and v2:", v1.dot(v2.T))

# Orthonormal vectors, orthonormal means that the norm of the vectors is 1.
print("Norm of v1:", np.linalg.norm(v1))
print("Norm of v2:", np.linalg.norm(v2))

v1 = np.array([[1, 0]])
v2 = np.array([[0, -1]])
print("Orthonormal vector v1:", v1)
print("Orthonormal vector v2:", v2)
print("Dot product of orthonormal v1 and v2:", v1.dot(v2.T))
print("Norm of orthonormal v1:", np.linalg.norm(v1))
print("Norm of orthonormal v2:", np.linalg.norm(v2))