#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


ax = new_subplots_math(1, 1, lim=[-20,20], step=2)

b = np.arange(0.1, 20, 0.1)
a = (b+3) / (b-1)
y = a*b

ax[0][0].plot(b, y)

plt.tight_layout()
plt.show()
