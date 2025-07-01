#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 1, lim=[-4,4])

x = np.arange(-5, 5, 0.1)
y = (-2) * (0.5**np.abs(x)) + 2
ax[0][0].plot(x, y)

plt.tight_layout()
plt.show()
