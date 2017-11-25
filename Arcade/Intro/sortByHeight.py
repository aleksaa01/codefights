def sortByHeight(a):
    trees = [i for i in range(len(a)) if a[i] == -1]
    for i in range(len(trees)):
        a.remove(-1)
    a.sort()
    
    for i in trees:
        a.insert(i, -1)
    return a


"""
Some people are standing in a row in a park. There are trees between them
which cannot be moved. Your task is to rearrange the people by their heights
in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""
