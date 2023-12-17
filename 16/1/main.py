from collections import deque
from enum import Enum
import numpy as np


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def go_up(q, visited_squares, row, column):
    if row > 0 and (row - 1, column, Direction.UP) not in visited_squares:
        q.appendleft((row - 1, column, Direction.UP))


def go_right(q, visited_squares, shape, row, column):
    if column < shape[1] - 1 and (row, column + 1, Direction.RIGHT) not in visited_squares:
        q.appendleft((row, column + 1, Direction.RIGHT))


def go_down(q, visited_squares, shape, row, column):
    if row < shape[0] - 1 and (row + 1, column, Direction.DOWN) not in visited_squares:
        q.appendleft((row + 1, column, Direction.DOWN))


def go_left(q, visited_squares, row, column):
    if column > 0 and (row, column - 1, Direction.LEFT) not in visited_squares:
        q.appendleft((row, column - 1, Direction.LEFT))


def process_laser(q, grid, energized_grid, visited_squares, row: int, column: int, direction: Direction):
    energized_grid[row, column] = 1
    e = grid[row, column]
    visited_squares.append((row, column, direction))

    if e == '.':
        if direction == Direction.UP:
            go_up(q, visited_squares, row, column)
        elif direction == Direction.RIGHT:
            go_right(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.DOWN:
            go_down(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.LEFT:
            go_left(q, visited_squares, row, column)
    elif e == '|':
        if direction == Direction.UP:
            go_up(q, visited_squares, row, column)
        elif direction == Direction.RIGHT:
            go_up(q, visited_squares, row, column)
            go_down(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.DOWN:
            go_down(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.LEFT:
            go_up(q, visited_squares, row, column)
            go_down(q, visited_squares, grid.shape, row, column)
    elif e == '\\':
        if direction == Direction.UP:
            go_left(q, visited_squares, row, column)
        elif direction == Direction.RIGHT:
            go_down(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.DOWN:
            go_right(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.LEFT:
            go_up(q, visited_squares, row, column)
    elif e == '/':
        if direction == Direction.UP:
            go_right(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.RIGHT:
            go_up(q, visited_squares, row, column)
        elif direction == Direction.DOWN:
            go_left(q, visited_squares, row, column)
        elif direction == Direction.LEFT:
            go_down(q, visited_squares, grid.shape, row, column)
    elif e == '-':
        if direction == Direction.UP:
            go_left(q, visited_squares, row, column)
            go_right(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.RIGHT:
            go_right(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.DOWN:
            go_left(q, visited_squares, row, column)
            go_right(q, visited_squares, grid.shape, row, column)
        elif direction == Direction.LEFT:
            go_left(q, visited_squares, row, column)


data = []
for line in open('../input.txt'):
    data.append([*line.strip()])
grid = np.array(data)
energized_grid = np.zeros_like(grid, dtype=int)
visited_squares = []
print(grid)

q = deque([(0, 0, Direction.RIGHT)])

while q:
    value = q.popleft()
    process_laser(q, grid, energized_grid, visited_squares, value[0], value[1], value[2])

print(energized_grid)
print(np.sum(energized_grid))
