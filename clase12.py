import numpy as np
import matplotlib.pyplot as plt

# Create a range of x values
x = np.arange(-5, 5)

# Define the linear functions
y_1 = 3*x + 5
y_2 = 2*x + 3

# Plot the functions
plt.figure()
plt.plot(x, y_1)
plt.plot(x, y_2)

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Functions')
plt.legend(['y = 3x + 5', 'y = 2x + 3'])
plt.grid()
plt.show()

# Solve the system of equations
A = np.array([[-3, 1], [-2, 1]])
B = np.array([[5], [3]])
sol_1 = np.array([-2, 1])
print(A.dot(sol_1))