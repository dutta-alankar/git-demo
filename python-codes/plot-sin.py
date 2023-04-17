import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0, 30, 100)
plt.plot(x, np.sin(x))
plt.ylabel("sin(x)")
plt.xlabel("x")
plt.grid()
plt.show()
