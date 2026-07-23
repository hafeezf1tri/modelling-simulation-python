import numpy as np
import matplotlib.pyplot as plt

# Differential equation: dy/dx = y
def f(x, y):
    return y

# Exact solution
def exact(x):
    return np.exp(x)

# Initial condition
x0 = 0
y0 = 1

# Step size
h = 0.6

# End of interval
x_end = 20

# Number of steps
n_steps = int((x_end - x0) / h)

# Euler method
x = [x0]
y = [y0]

for i in range(n_steps):
    x_new = x[-1] + h
    y_new = y[-1] + h * f(x[-1], y[-1])

    x.append(x_new)
    y.append(y_new)

# Exact solution for plotting
x_exact = np.linspace(x0, x_end, 200)
y_exact = exact(x_exact)

# Print table
print(" x      Euler       Exact")
print("-----------------------------")
for xi, yi in zip(x, y):
    print(f"{xi:3.1f}   {yi:8.5f}   {exact(xi):8.5f}")

# Plot
plt.figure(figsize=(7,5))
plt.plot(x_exact, y_exact, label="Exact Solution")
plt.plot(x, y, 'o--', label="Euler Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler Method")
plt.grid(True)
plt.legend()
plt.show()
