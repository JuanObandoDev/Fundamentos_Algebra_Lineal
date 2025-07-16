import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

v1 = np.array([2, 7])
v2 = np.array([3, 5])
print("Vector v1:", v1)
print("Vector v2:", v2)

v1v2 = v1+v2
print("Vector v1 + v2:", v1v2)

# norm(v1v2) <= norm(v1) + norm(v2)
print("Norm of v1:", np.linalg.norm(v1))
print("Norm of v2:", np.linalg.norm(v2))
print("Norm of v1 + v2:", np.linalg.norm(v1v2))
print(np.linalg.norm(v1v2) <= (np.linalg.norm(v1) + np.linalg.norm(v2)))
print(np.linalg.norm(v1) + np.linalg.norm(v2))

v1 = np.array([0, 0, 2, 7])
v2 = np.array([0, 0, 3, 5])

v1_aux = np.array([v1[2], v1[3], v2[2], v2[3]])
v1v2 = np.array([0, 0, 5, 12])
plt.quiver(
    [v1[0], v1_aux[0], v1v2[0]], 
    [v1[1], v1_aux[1], v1v2[1]], 
    [v1[2], v1_aux[2], v1v2[2]], 
    [v1[3], v1_aux[3], v1v2[3]], 
    angles='xy', 
    scale_units='xy', 
    scale=1, 
    color=sns.color_palette()
)
plt.xlim(-0.5, 6)
plt.ylim(-0.5, 15)
plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
plt.title("Vector Addition")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(['v1', 'v2', 'v1 + v2'])
plt.show()