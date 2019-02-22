def sudoku2(grid):

    def duplicates(s):
        for i in '123456789':
            if s.count(i) > 1:
                return False
        return True

    for i in grid:
        if not duplicates(i):
            return False
    for j in zip(*grid):
        if not duplicates(j):
            return False

    lst1, lst2, lst3 = [], [], []
    for i in range(9):
        for j in range(9):
            if j == 0 or j == 1 or j == 2:
                lst1.append(grid[i][j])
            elif j == 3 or j == 4 or j == 5:
                lst2.append(grid[i][j])
            else:
                lst3.append(grid[i][j])

    for i in range(0, 27, 9):
        if not (duplicates(lst1[i:i + 9]) and duplicates(lst2[i:i + 9]) and duplicates(lst3[i:i + 9])):
            return False
    return True


"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column,
each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers
from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to
the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3
subgrid can only contain the numbers 1 through 9 one time.
"""