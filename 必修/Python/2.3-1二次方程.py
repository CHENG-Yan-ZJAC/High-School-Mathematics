#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 3)

x = np.arange(-5, 5, 0.1)

y1 = x**2
y2 = 2 * x**2
ax[0][0].plot(x, y1, linestyle='-',  label='a=1')
ax[0][0].plot(x, y2, linestyle='--', label='a=2')
ax[0][0].legend(fontsize=20)

y1 = x**2
y2 = (x+1)**2
ax[0][1].plot(x, y1, linestyle='-',  label='b=0')
ax[0][1].plot(x, y2, linestyle='--', label='b=1')
ax[0][1].legend(fontsize=20)

y1 = x**2
y2 = x**2 + 1
ax[0][2].plot(x, y1, linestyle='-',  label='c=0')
ax[0][2].plot(x, y2, linestyle='--', label='c=1')
ax[0][2].legend(fontsize=20)

plt.tight_layout()
plt.show()
