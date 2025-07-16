import numpy as np
import matplotlib.pyplot as plt
from utils.graph_vectors import graph_vectors

v1 = np.array([2, 5])
v2 = np.array([3, 2])

graph_vectors([v1, v2], ['orange', 'blue'])
plt.xlim(-1, 8)
plt.ylim(-1, 8)
plt.title("Vectors v1 and v2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(['v1', 'v2'])
plt.show()