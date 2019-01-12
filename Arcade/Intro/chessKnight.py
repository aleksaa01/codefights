def check_pos(cell, pos):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    return (0 < d[cell[0]] + pos[0] <= 8) and (0 < int(cell[1]) + pos[1] <= 8)


def chessKnight(cell):
    # clockwise
    positions = [
        (1, 2), (2, 1),
        (2, -1), (1, -2),
        (-1, -2), (-2, -1),
        (-2, 1), (-1, 2)
    ]

    res = 0
    for pos in positions:
        if check_pos(cell, pos):
            res += 1

    return res


"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares
vertically and one square horizontally away from it. The complete move therefore looks like the letter L.
Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

Example

    For cell = "a1", the output should be
    chessKnight(cell) = 2.
    For cell = "c2", the output should be
    chessKnight(cell) = 6.
"""