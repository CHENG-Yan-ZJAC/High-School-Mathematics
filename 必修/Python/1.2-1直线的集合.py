#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 2)

x = np.arange(-5, 5, 0.1)
y = x
ax[0][0].plot(x, y)

x  = np.arange(-5, 5, 0.1)
y1 = 2*x - 1
y2 = (5 - x) / 4
ax[0][1].plot(x, y1)
ax[0][1].plot(x, y2)

plt.tight_layout()
plt.show()
