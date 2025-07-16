import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = np.array([1, 1])
v2 = np.array([-1, -1])
# for a in range(-10, 10):
#     for b in range(-10, 10):
#         plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a + v2[1]*b, marker ='.', color='orange')

# plt.xlim(-25, 25)
# plt.ylim(-25, 25)
# plt.axvline(x=0, color='grey')
# plt.axhline(y=0, color='grey')
# plt.show()

v1 = np.array([1, 0])
v2 = np.array([2, -3])
# for a in range(-10, 10):
#     for b in range(-10, 10):
#         plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a + v2[1]*b, marker ='.', color='orange')

# plt.xlim(-25, 25)
# plt.ylim(-25, 25)
# plt.axvline(x=0, color='grey')
# plt.axhline(y=0, color='grey')
# plt.show()

v1 = np.array([1, 0, 0])
v2 = np.array([2, -3, 0])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for a in range(-10, 10):
    for b in range(-10, 10):
        ax.scatter(v1[0]*a + v2[0]*b, v1[1]*a + v2[1]*b, v1[2]*a + v2[2]*b, marker ='.', color='orange')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.show()