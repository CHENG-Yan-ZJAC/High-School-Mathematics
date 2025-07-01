#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 1)

x  = np.arange(0.1, 5, 0.1)
y1 = x + 0.5/x
y2 = x + 1/x
y3 = x + 2/x

ax[0][0].plot(x, y1, linestyle='-',  label='b=0.5')
ax[0][0].plot(x, y2, linestyle='--', label='b=1')
ax[0][0].plot(x, y3, linestyle='-.', label='b=2')

plt.legend(fontsize=20)
plt.tight_layout()
plt.show()
