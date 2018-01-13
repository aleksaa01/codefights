def chessBoardCellColor(cell1, cell2):
    d = {}
    first_color = 'a'
    second_color = 'b'
    color  = None
    for i, e in enumerate("ABCDEFGH"):
        if i % 2 == 0:
            color = 'a'
        else:
            color = 'b'
        for i in range(1,9):
            k = e + str(i)
            d[k] = color
            if color == 'a':
                color = 'b'
            else:
                color = 'a'
    return d[cell1] == d[cell2]


"""
Given two cells on the standard chess board, determine whether they have the
same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.


"""
