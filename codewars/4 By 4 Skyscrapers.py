import copy
import functools

global n, row_clues, column_clues, grid
globals()['n'] = 4


def visible_number(a):
    number1 = len(functools.reduce(lambda x, v: x.union({max(v, max(x))}), a, {0})) - 1
    number2 = len(functools.reduce(lambda x, v: x.union({max(v, max(x))}), list(reversed(a)), {0})) - 1
    return [number1, number2]


def is_valid(grid_):
    satisfy = lambda v, clue: visible_number(v) == clue
    # checks if all rows satisfy its clues
    if not functools.reduce(lambda x, i, c=row_clues: x and satisfy(grid_[i], c[i]), range(n), True):
        return False
    # same with columns
    return functools.reduce(lambda x, i, c=column_clues: x and satisfy(list(zip(*grid_))[i], c[i]), range(n), True)


def calculate_next_position(grid_, pos):
    for i in range(n):
        for j in range(n):
            if i == pos[0] and j == pos[1]:
                continue
            if grid_[i][j] == 0:
                return [i, j]
    return [n, n]


def fill_pos(grid_, pos):
    if pos[0] == pos[1] == n:
        print(grid_)
        return grid_
    next_pos = calculate_next_position(grid_, pos)
    for value in range(1, n + 1):
        next_grid = copy.deepcopy(grid)
        next_grid[pos[0]][pos[1]] = value
        if is_valid(next_grid):
            return fill_pos(next_grid, next_pos)


def fill():
    global grid
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(row_clues)):
        for j in range(2):
            if row_clues[i][j] == 1:
                grid[i][0 if j == 0 else n - 1] = n
            elif row_clues[i][j] == n:
                iterator = range(1, n+1) if j == 0 else range(n, 0, -1)
                grid[i] = list(iterator)
    return fill_pos(grid, calculate_next_position(grid, [-1, -1]))


def solve_puzzle(clues):
    global row_clues, column_clues
    row_clues = [[clues[i], clues[3 * n - 1 - i]] for i in range(n)]
    column_clues = [[clues[5 * n - 1 - i], clues[i]] for i in range(n, 2 * n)]
    return fill()


test_clues = (2, 2, 1, 3,
              2, 2, 3, 1,
              1, 2, 2, 3,
              3, 2, 1, 3)

a = [[2, 3], [2, 2], [1, 2], [3, 1]]
b = [[3, 2], [1, 2], [2, 3], [3, 1]]
'''test_grid = ((1, 3, 4, 2),
                (4, 2, 1, 3),
                (3, 4, 2, 1),
                (2, 1, 3, 4))'''
# print(solve_puzzle(test_clues))
q = lambda x: [k for k in range(1, n+1) if k != x]
print(q(4))
