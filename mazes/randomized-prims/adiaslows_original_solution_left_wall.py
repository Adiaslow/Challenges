#!/usr/bin/env python 3.10

"""Create your maze solver here."""

import matplotlib.pyplot as plt
import numpy as np
import time

import randomized_prims_maze_generator as prims


HEIGHT = 100
WIDTH = 100

maze = prims.maze_gen(HEIGHT, WIDTH)

start_time = time.time()

START = (0, 1)
END = (-1, -2)

maze[START] = 1
maze[END] = 1

current_loc = START
facing = "S"
steps_taken = 0

solved = False

while not solved:
    if current_loc == END:
        print("Solved!")
        solved = True

    NORTH = (current_loc[0] - 1, current_loc[1])
    SOUTH = (current_loc[0] + 1, current_loc[1])
    EAST = (current_loc[0], current_loc[1] + 1)
    WEST = (current_loc[0], current_loc[1] - 1)

    maze[current_loc] = 0.5

    try:
        if facing == "S":
            if maze[EAST] != 0:
                current_loc = EAST
                facing = "E"

            elif maze[SOUTH] != 0:
                current_loc = SOUTH
                facing = "S"

            elif maze[WEST] != 0:
                current_loc = WEST
                facing = "W"

            elif maze[NORTH] != 0:
                current_loc = NORTH
                facing = "N"

        elif facing == "W":
            if maze[SOUTH] != 0:
                current_loc = SOUTH
                facing = "S"

            elif maze[WEST] != 0:
                current_loc = WEST
                facing = "W"

            elif maze[NORTH] != 0:
                current_loc = NORTH
                facing = "N"

            elif maze[EAST] != 0:
                current_loc = EAST
                facing = "E"

        elif facing == "N":
            if maze[WEST] != 0:
                current_loc = WEST
                facing = "W"

            elif maze[NORTH] != 0:
                current_loc = NORTH
                facing = "N"

            elif maze[EAST] != 0:
                current_loc = EAST
                facing = "E"

            elif maze[SOUTH] != 0:
                current_loc = SOUTH
                facing = "S"

        elif facing == "E":
            if maze[NORTH] != 0:
                current_loc = NORTH
                facing = "N"

            elif maze[EAST] != 0:
                current_loc = EAST
                facing = "E"

            elif maze[SOUTH] != 0:
                current_loc = SOUTH
                facing = "S"

            elif maze[WEST] != 0:
                current_loc = WEST
                facing = "W"

    except IndexError:
            print("Solved!")
            print(f"Steps Taken = {steps_taken}")
            solved = True


    steps_taken += 1
    # print(steps_taken)
    # print(current_loc)
    # print(facing)

    if steps_taken > 1000000:
        break


end_time = time.time()
print("Run Time = " + str(end_time - start_time))
print()

print(maze)
plt.imshow(maze, cmap='gnuplot2')
plt.show()
