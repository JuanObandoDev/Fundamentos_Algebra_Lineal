import numpy as np
import matplotlib.pyplot as plt

# OVERDETERMINED system (more equations than variables) no solution
x = np.arange(-6, 6)
y_1 = 3 * x + 5
y_2 = -x + 3
y_3 = 2 * x + 1

# plt.figure()
# plt.plot(x, y_1)
# plt.plot(x, y_2)
# plt.plot(x, y_3)
# plt.xlim(-8, 8)
# plt.ylim(-8, 8)
# plt.axvline(0, color='grey')
# plt.axhline(0, color='grey')
# plt.grid()
# plt.title("Graph of Linear Equations")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend(['y = 3x + 5', 'y = -x + 3', 'y = 2x + 1'])
# plt.show()

# DETERMINED system, unique solution with same y_2 and y_3 from previous example (same vaiables than equations)
# plt.figure()
# plt.plot(x, y_2)
# plt.plot(x, y_3)
# plt.xlim(-8, 8)
# plt.ylim(-8, 8)
# plt.axvline(0, color='grey')
# plt.axhline(0, color='grey')
# plt.grid()
# plt.title("Graph of Linear Equations")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend(['y = -x + 3', 'y = 2x + 1'])
# plt.show()

# INDETERMINED system, infinitely many solutions (same line) (less equations than variables)
plt.figure()
plt.plot(x, y_3)
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.axvline(0, color='grey')
plt.axhline(0, color='grey')
plt.grid()
plt.title("Graph of Linear Equations")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(['y = -x + 3', 'y = 2x + 1'])
plt.show()