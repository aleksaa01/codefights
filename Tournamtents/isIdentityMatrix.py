def isIdentityMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                if matrix[i][i] != 1:
                    return False
            elif matrix[i][j] != 0:
                return False
    return True



"""
Check if the given matrix is an identity matrix.
"""