#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(2, 2, lim=[-4,4])

x = np.arange(0, 5, 0.1)

y1 = 0.5**x
y2 = 0.5**(x-1)
y3 = (-1)*0.5**(x-1)
y4 = (-1)*0.5**(x-1) + 2

ax[0][0].plot(x, y1)
ax[0][0].annotate(r'$y=\left( \frac{1}{2} \right) ^x$', (-3, 3), fontsize=16)
ax[0][1].plot(x, y2)
ax[0][1].annotate(r'$y=\left( \frac{1}{2} \right) ^{x-1}$', (-3, 3), fontsize=16)
ax[1][0].plot(x, y3)
ax[1][0].annotate(r'$y=-\left( \frac{1}{2} \right) ^{x-1}$', (-3.5, 3), fontsize=16)
ax[1][1].plot(x, y4)
ax[1][1].annotate(r'$y=-\left( \frac{1}{2} \right) ^{x-1}+2$', (-3.5, 3), fontsize=16)

plt.tight_layout()
plt.show()
