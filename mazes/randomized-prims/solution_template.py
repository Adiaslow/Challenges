#!/usr/bin/env python 3.10

"""Create your maze solver here."""

import matplotlib.pyplot as plt
import time

import randomized_prims_maze_generator as prims

start_time = time.time()

HEIGHT = 100
WIDTH = 100

maze = prims.maze_gen(HEIGHT, WIDTH)

START = (0, 1)
END = (-1, -2)

maze[START] = 0.4
maze[END] = 0.6


end_time = time.time()
print("Run Time = " + str(end_time-start_time))
print()

print(maze)
plt.imshow(maze, cmap='gnuplot2')
plt.show()
