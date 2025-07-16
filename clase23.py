import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

v1 = np.array([0, 0, 0, 3])
v2 = np.array([0, 0, 3, 3])

plt.xlim(-2, 6)
plt.ylim(-2, 6)
plt.quiver(
    [v1[0], v2[0]],
    [v1[1], v2[1]],
    [v1[2], v2[2]],
    [v1[3], v2[3]],
    angles='xy',
    scale_units='xy',
    scale=1,
    color=sns.color_palette()
)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
plt.title("Vector Addition")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(['v1', 'v2'])
plt.show()

v1 = np.array([0, 3])
v2 = np.array([3, 3])
print(v1.T.dot(v2))

norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)
print(norm_v1 * norm_v2 * np.cos(np.deg2rad(45)))