import sys


def deepcopy(grid):
    return [row[:] for row in grid]


def print_grid(grid):
    for line in grid:
        print(line)


def read_grid():
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    return grid


def out_of_bounds(grid, i, j):
    n, m = len(grid), len(grid[0])
    return i < 0 or n <= i or j < 0 or m <= j


def nan(grid, i, j):
    # print(f'i={i} < 0', i < 0)
    # print(f'n <= i={i}', n <= i)
    # print(f'j={j} < 0', j < 0)
    # print(f'm >= j={j}', m >= j)
    if out_of_bounds(grid, i, j):
        return True
    char = grid[i][j]
    return char == '.' or is_symbol(char) or char == 'x'


def is_symbol(char):
    return not (char.isdigit() or char == '.' or char == 'x')


def get_num(grid, i, j, l, r):
    str = ''.join(grid[i][j-l:j+r+1])
    return int(str) if str.isnumeric() else 0


def zero_out(grid, i, j, l, r):
    for k in range(j-l, j+r+1):
        grid[i][k] = 'x'


def explore_number(grid, i, j):
    if out_of_bounds(grid, i, j):
        return 0

    # print('explore number', i, j)
    # offsets
    l = 0
    r = 0
    while True:
        # explore left
        if nan(grid, i, j-l-1):
            break
        l += 1

    while True:
        # explore right
        if nan(grid, i, j+r+1):
            break
        r += 1

    num = get_num(grid, i, j, l, r)
    # print(f'get_num(grid, {i}, {j}, {l}, {r}) -> {num}')
    if num > 0:
        zero_out(grid, i, j, l, r)
    # print_grid(grid)
    # print('returning from explore_number')
    return num


def explore_symbol(grid, i, j):
    """

    Gets all the numbers around the symbol at grid[i][j], and marks those
    numbers with an x

    """
    num1 = explore_number(grid, i, j-1) # left
    num2 = explore_number(grid, i-1, j-1) # upper left
    num3 = explore_number(grid, i-1, j) # up
    num4 = explore_number(grid, i-1, j+1) # upper right
    num5 = explore_number(grid, i, j+1) # right
    num6 = explore_number(grid, i+1, j+1) # lower right
    num7 = explore_number(grid, i+1, j) # down
    num8 = explore_number(grid, i+1, j-1) # lower right

    results = [num1, num2, num3, num4, num5, num6, num7, num8]
    nonzero_results = [n for n in results if n > 0]

    if len(nonzero_results) == 2:
        return nonzero_results[0] * nonzero_results[1]
    else:
        return 0


if __name__ == '__main__':
    grid = read_grid()
    original_grid = deepcopy(grid)

    n, m = len(grid), len(grid[0])
    # print('n, m', n, m)

    num_sum = 0
    for i in range(n):
        for j in range(m):
            # print(i, j)
            # print_grid(grid)
            if grid[i][j] == '*':
                # print(f'grid[{i}][{j}] is a symbol!', i, j, grid[i][j])
                sum = explore_symbol(grid, i, j) # modifies grid
                num_sum += sum
            grid = original_grid
    # print_grid(grid)
    print(num_sum)
