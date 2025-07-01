#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 2, lim=[-4,4])

x = np.arange(-5, 5, 0.1)

y1 = 2**x
y2 = 3**x
y3 = 4**x
ax[0][0].plot(x, y1, linestyle='-',  label='a=2')
ax[0][0].plot(x, y2, linestyle='--', label='a=3')
ax[0][0].plot(x, y3, linestyle='-.', label='a=4')
ax[0][0].legend(fontsize=20)

y1 = (1/2)**x
y2 = (1/3)**x
y3 = (1/4)**x
ax[0][1].plot(x, y1, linestyle='-',  label='a=1/2')
ax[0][1].plot(x, y2, linestyle='--', label='a=1/3')
ax[0][1].plot(x, y3, linestyle='-.', label='a=1/4')
ax[0][1].legend(fontsize=20)

plt.tight_layout()
plt.show()
