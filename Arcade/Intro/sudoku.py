def sudoku(grid):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # check rows
    for row in grid:
        if sorted(row) != nums:
            return False

    # check columns
    for column in zip(*grid):
        if sorted(column) != nums:
            return False

    # check quads
    for i in range(0, 6, 3):
        l1, l2, l3 = grid[i:i + 3]
        for j in range(0, 6, 3):
            if sorted(l1[j:j + 3] + l2[j:j + 3] + l3[j:j + 3]) != nums:
                return False

    return True


"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column,
each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For the first example below, the output should be true. For the other grid, the output should be false:
each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
"""