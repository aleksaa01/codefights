def unique_append(unique_lst, lst):
    for i in unique_lst:
        if i == lst:
            return
    unique_lst.append(lst)


def differentSquares(matrix):
    unique = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            row1, row2 = matrix[i][j], matrix[i][j + 1]
            row3, row4 = matrix[i + 1][j], matrix[i + 1][j + 1]
            unique_append(unique, [row1, row2, row3, row4])

    return len(unique)


"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

    1 2
    2 2
    2 1
    2 2
    2 2
    2 2
    2 2
    1 2
    2 2
    2 3
    2 3
    2 1

"""