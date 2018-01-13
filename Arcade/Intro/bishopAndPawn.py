def bishopAndPawn(bishop, pawn):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    return d[bishop[0]] + int(bishop[1]) == d[pawn[0]] + int(pawn[1]) or abs(d[bishop[0]] - int(bishop[1])) == abs(d[pawn[0]] - int(pawn[1]))



"""
Given the positions of a white bishop and a black pawn on the standard chess
board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to
diagonal movement. Check out the example below to see how it can move:


Example

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.



For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.


"""
