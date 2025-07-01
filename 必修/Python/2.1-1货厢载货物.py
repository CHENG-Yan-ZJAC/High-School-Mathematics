#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 1, lim=[-80,80], step=10)

x  = np.arange(-100, 100, 0.1)
yA = (1530 - 35*x) / 25
yB = (1150 - 15*x) / 35
yT = 50 - x
yC = -0.5*x / 0.8

ax[0][0].plot(x, yA, linestyle='-',  label='Goods JIA')
ax[0][0].plot(x, yB, linestyle='-.', label='Goods YI')
ax[0][0].plot(x, yT, linestyle=':',  label='Total Cargo')
ax[0][0].plot(x, yC, linestyle='--', label='Total Price')

ax[0][0].annotate('M', (-10,  60), fontsize=18)
ax[0][0].annotate('P', ( 30,  20), fontsize=18)
ax[0][0].annotate('N', ( 75, -7),  fontsize=18)

plt.legend(fontsize=20)
plt.tight_layout()
plt.show()
