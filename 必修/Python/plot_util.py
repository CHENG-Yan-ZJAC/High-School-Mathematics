#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA


def new_subplots(row:int, col:int):
	figsize = (4, 2)
	if row == 1 and col == 1:
		figsize = (4, 2)
	elif row == 2 and col == 1:
		figsize = (6, 4)
	elif row == 2 and col == 2:
		figsize = (8, 4)
	elif row == 2 and col == 3:
		figsize = (10, 4)
	elif row == 3 and col == 1:
		figsize = (6, 4)
	elif row == 3 and col == 2:
		figsize = (8, 4)
	else:
		print('unknown row={} and col={}'.format(row, col))
		pass

	fig, axs = plt.subplots(row, col, figsize=figsize)
	return axs


def new_subplots_math(row:int, col:int, lim:list=[-5,5], step:int=1):
	axs = []

	# create figure
	if row == 1 and col == 1:
		figsize = (6, 6)
	elif row == 1 and col == 2:
		figsize = (8, 4)
	elif row == 2 and col == 2:
		figsize = (8, 8)
	elif row == 1 and col == 3:
		figsize = (12, 4)
	else:
		print('unknown row={} and col={}'.format(row, col))
		return
	fig = plt.figure(figsize=figsize)

	# for every row
	for r in range(row):
		axs_r = []

		# for every column
		for c in range(col):
			# new a subplot without axis
			ax = fig.add_subplot(row, col, r*col+c+1, axes_class=AA.Axes)
			ax.axis[:].set_visible(False)
			ax.set_aspect('equal')

			# plot x axis
			ax.axis['x'] = ax.new_floating_axis(0, 0)
			ax.axis['x'].set_axisline_style('->')
			ax.axis['x'].set_axis_direction('top')
			# set limit
			ax.set_xlim(lim)
			# draw ticks
			ticks = []
			label = []
			for i in range(lim[0], lim[1]+1, step):
				if i != 0:
					ticks.append(i)
					label.append(str(i))
					pass
				pass
			ax.set_xticks(ticks, label)

			# plot y axis
			ax.axis['y'] = ax.new_floating_axis(1, 0)
			ax.axis['y'].set_axisline_style('->')
			ax.axis['y'].set_axis_direction('right')
			# set limit
			ax.set_ylim(lim)
			# draw ticks
			ticks = []
			label = []
			for i in range(lim[0], lim[1]+1, step):
				if i != 0:
					ticks.append(i)
					label.append(str(i))
					pass
				pass
			ax.set_yticks(ticks, label)

			axs_r.append(ax)
			pass

		axs.append(axs_r)
		pass

	return axs
