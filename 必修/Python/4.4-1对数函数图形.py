#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 2, lim=[-4,4])

x = np.arange(0.1, 5, 0.1)

y1 = np.log(x) / np.log(2)
y2 = np.log(x) / np.log(3)
y3 = np.log(x) / np.log(4)
ax[0][0].plot(x, y1, linestyle='-',  label='a=2')
ax[0][0].plot(x, y2, linestyle='--', label='a=3')
ax[0][0].plot(x, y3, linestyle='-.', label='a=4')
ax[0][0].legend(fontsize=20)

y1 = np.log(x) / np.log(1/2)
y2 = np.log(x) / np.log(1/3)
y3 = np.log(x) / np.log(1/4)
ax[0][1].plot(x, y1, linestyle='-',  label='a=1/2')
ax[0][1].plot(x, y2, linestyle='--', label='a=1/3')
ax[0][1].plot(x, y3, linestyle='-.', label='a=1/4')
ax[0][1].legend(fontsize=20)

plt.tight_layout()
plt.show()
