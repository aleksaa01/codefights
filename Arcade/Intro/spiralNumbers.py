def spiralNumbers(n):
    def recover_xy(x, y, index):
        if index == 0:
            y -= 1
            x += 1
        elif index == 1:
            x -= 1
            y -= 1
        elif index == 2:
            y += 1
            x -= 1
        elif index == 3:
            x += 1
            y += 1
        return x, y

    def update_xy(x, y, index):
        if index == 0:
            y += 1
        elif index == 1:
            x += 1
        elif index == 2:
            y -= 1
        elif index == 3:
            x -= 1
        return x, y

    # 1=[x][y++], 2=[x++][y], -1=[x][y--], -2=[x--][y]
    movs = [1, 2, -1, -2]
    mov_index = 0

    matrix = [[0] * n for _ in range(n)]

    x = 0
    y = 0
    for i in range(n * n):

        if y >= n or x >= n or y < 0 or matrix[x][y] != 0:
            x, y = recover_xy(x, y, mov_index)
            mov_index = (mov_index + 1) % 4

        matrix[x][y] = i + 1
        x, y = update_xy(x, y, mov_index)

    return matrix


"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order,
starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]

"""