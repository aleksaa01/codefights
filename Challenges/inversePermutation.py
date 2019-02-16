def inversePermutation(permutation):
    invperm = [0] * len(permutation)
    for i in range(len(permutation)):
        invperm[permutation[i] - 1] = i + 1

    return invperm



"""
Given a permutation, produce its inverse permutation.

Example

For permutation = [1, 3, 4, 2], the output should be
inversePermutation(permutation) = [1, 4, 2, 3].
"""