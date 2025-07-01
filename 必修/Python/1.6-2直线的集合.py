#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 2)

x  = np.arange(-5, 5, 0.1)
yA =  2*x
yB = -3*x
yC =  2*x - 3

ax[0][0].plot(x, yA)
ax[0][0].plot(x, yB)

ax[0][1].plot(x, yA)
ax[0][1].plot(x, yC)

plt.tight_layout()
plt.show()
