from enum import Enum
import numpy as np


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def process_laser(grid, energized_grid, visited_squares, row: int, column: int, direction: Direction):
    if (row, column, direction) in visited_squares or row < 0 or column < 0 or row >= grid.shape[0] or column >= grid.shape[0]:
        return
    energized_grid[row, column] = 1
    e = grid[row, column]
    visited_squares.append((row, column, direction))
    if e == '.':
        if direction == Direction.UP:
            process_laser(grid, energized_grid, visited_squares, row - 1, column, Direction.UP)
        elif direction == Direction.RIGHT:
            process_laser(grid, energized_grid, visited_squares, row, column + 1, Direction.RIGHT)
        elif direction == Direction.DOWN:
            process_laser(grid, energized_grid, visited_squares, row + 1, column, Direction.DOWN)
        elif direction == Direction.LEFT:
            process_laser(grid, energized_grid, visited_squares, row, column - 1, Direction.LEFT)
    elif e == '|':
        if direction == Direction.UP:
            process_laser(grid, energized_grid, visited_squares, row - 1, column, Direction.UP)
        elif direction == Direction.RIGHT:
            process_laser(grid, energized_grid, visited_squares, row - 1, column, Direction.UP)
            process_laser(grid, energized_grid, visited_squares, row + 1, column, Direction.DOWN)
        elif direction == Direction.DOWN:
            process_laser(grid, energized_grid, visited_squares, row + 1, column, Direction.DOWN)
        elif direction == Direction.LEFT:
            process_laser(grid, energized_grid, visited_squares, row - 1, column, Direction.UP)
            process_laser(grid, energized_grid, visited_squares, row + 1, column, Direction.DOWN)
    elif e == '\\':
        if direction == Direction.UP:
            process_laser(grid, energized_grid, visited_squares, row, column - 1, Direction.LEFT)
        elif direction == Direction.RIGHT:
            process_laser(grid, energized_grid, visited_squares, row + 1, column, Direction.DOWN)
        elif direction == Direction.DOWN:
            process_laser(grid, energized_grid, visited_squares, row, column + 1, Direction.RIGHT)
        elif direction == Direction.LEFT:
            process_laser(grid, energized_grid, visited_squares, row - 1, column, Direction.UP)
    elif e == '/':
        if direction == Direction.UP:
            process_laser(grid, energized_grid, visited_squares, row, column + 1, Direction.RIGHT)
        elif direction == Direction.RIGHT:
            process_laser(grid, energized_grid, visited_squares, row - 1, column, Direction.UP)
        elif direction == Direction.DOWN:
            process_laser(grid, energized_grid, visited_squares, row, column - 1, Direction.LEFT)
        elif direction == Direction.LEFT:
            process_laser(grid, energized_grid, visited_squares, row + 1, column, Direction.DOWN)
    elif e == '-':
        if direction == Direction.UP:
            process_laser(grid, energized_grid, visited_squares, row, column - 1, Direction.LEFT)
            process_laser(grid, energized_grid, visited_squares, row, column + 1, Direction.RIGHT)
        elif direction == Direction.RIGHT:
            process_laser(grid, energized_grid, visited_squares, row, column + 1, Direction.RIGHT)
        elif direction == Direction.DOWN:
            process_laser(grid, energized_grid, visited_squares, row, column - 1, Direction.LEFT)
            process_laser(grid, energized_grid, visited_squares, row, column + 1, Direction.RIGHT)
        elif direction == Direction.LEFT:
            process_laser(grid, energized_grid, visited_squares, row, column - 1, Direction.LEFT)


data = []
for line in open('../test.txt'):
    data.append([*line.strip()])
grid = np.array(data)
energized_grid = np.zeros_like(grid, dtype=int)
visited_squares = []
print(grid)

process_laser(grid, energized_grid, visited_squares, 0, 0, Direction.RIGHT)

print(energized_grid)
print(np.sum(energized_grid))
