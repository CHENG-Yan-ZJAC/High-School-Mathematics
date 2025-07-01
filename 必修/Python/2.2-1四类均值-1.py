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

fig, axs = plt.subplots(2, 2, figsize=(8,8), subplot_kw={'projection':'3d'})

axs[0][0].plot_wireframe(x, y, Hn, rstride=2, cstride=2)
axs[0][0].set_xlim(lim)
axs[0][0].set_ylim(lim)
axs[0][0].set_zlim(lim)
axs[0][0].set_xlabel(r'$x_1$')
axs[0][0].set_ylabel(r'$x_2$')
axs[0][0].set_zlabel(r'$H_n$')
axs[0][0].set_title(r'$H_n=\frac{2}{1/x_1+1/x_2}$')

axs[0][1].plot_wireframe(x, y, Gn, rstride=2, cstride=2)
axs[0][1].set_xlim(lim)
axs[0][1].set_ylim(lim)
axs[0][1].set_zlim(lim)
axs[0][1].set_xlabel(r'$x_1$')
axs[0][1].set_ylabel(r'$x_2$')
axs[0][1].set_title(r'$G_n=\sqrt{x_1x_2}$')

axs[1][0].plot_wireframe(x, y, An, rstride=2, cstride=2)
axs[1][0].set_xlim(lim)
axs[1][0].set_ylim(lim)
axs[1][0].set_zlim(lim)
axs[1][0].set_xlabel(r'$x_1$')
axs[1][0].set_ylabel(r'$x_2$')
axs[1][0].set_title(r'$A_n=\frac{x_1+x_2}{2}$')

axs[1][1].plot_wireframe(x, y, Qn, rstride=2, cstride=2)
axs[1][1].set_xlim(lim)
axs[1][1].set_ylim(lim)
axs[1][1].set_zlim(lim)
axs[1][1].set_xlabel(r'$x_1$')
axs[1][1].set_ylabel(r'$x_2$')
axs[1][1].set_title(r'$Q_n=\sqrt{\frac{{x_1}^2+{x_2}^2}{2}}$')

plt.tight_layout()
plt.show()
