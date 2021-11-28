from numpy import *
import matplotlib.pyplot as plt

x = linspace(0,5,500)
y = x**sin(10*x)

plt.plot(x, y)
plt.show()