import numpy as np
import matplotlib.pyplot as plt
from utils.graph_vectors import graph_vectors

v1 = np.array([2, 5])
v2 = np.array([3, 2])

v1v2 = 2*v1 + v2
print("2v1 + v2:\n", v1v2)

# graph_vectors([v1, v2, v1v2], ['orange', 'blue', 'red'])
# plt.xlim(-1, 8)
# plt.ylim(-1, 8)
# plt.title("Vectors v1, v2 and 2v1 + 3v2")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid()
# plt.legend(['v1', 'v2', '2v1 + 3v2'])
# plt.show()

for a in range(-10, 10):
    for b in range(-10, 10):
        plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a + v2[1]*b, marker ='.', color='orange')

plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
plt.show()