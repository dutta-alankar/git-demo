import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-30, 30, 200)
eps = 1e-5
plt.plot(x, (np.sin(x)+eps)/(x+eps))
plt.ylabel("sin(x)/x")
plt.xlabel("x")
plt.grid(ls=":")
plt.show()
