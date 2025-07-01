#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x   = np.arange(0, 5, 0.1)
y   = np.arange(0, 5, 0.1)
x,y = np.meshgrid(x, y)
lim = [0, 5]

An = (x + y) / 2
Hn = 2 / (1/x + 1/y)
Qn = np.sqrt((x**2 + y**2) / 2)
Gn = np.sqrt(x*y)

fig, ax = plt.subplots(1, 1, figsize=(6,6), subplot_kw={'projection':'3d'})

ax.plot_wireframe(x, y, Hn, rstride=2, cstride=2, label=r'$H_n$', color='b')
ax.plot_wireframe(x, y, Gn, rstride=2, cstride=2, label=r'$G_n$', color='g')
ax.plot_wireframe(x, y, An, rstride=2, cstride=2, label=r'$A_n$', color='orange')
ax.plot_wireframe(x, y, Qn, rstride=2, cstride=2, label=r'$Q_n$', color='r')
ax.set_xlim(lim)
ax.set_ylim(lim)
ax.set_zlim(lim)
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')

ax.legend()
plt.tight_layout()
plt.show()
