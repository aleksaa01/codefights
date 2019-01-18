def multiplicationTable(n):
    return [[i for i in range(j, j*n+1, j)] for j in range(1, n+1)]



"""
Looks like your little brother doesn't want to remember the multiplication table! Instead he wants to play
videogames all day long. To teach him a lesson you'd like to write a virus that will pop up in the middle of the
game and disappear only when the brother correctly solves several math questions.

To begin with, you need to construct a multiplication table. Given an integer n, return the
multiplication table of size n × n.

Example

For n = 5, the output should be

multiplicationTable(n) = [[1, 2,  3,  4,  5 ],
                          [2, 4,  6,  8,  10],
                          [3, 6,  9,  12, 15],
                          [4, 8,  12, 16, 20],
                          [5, 10, 15, 20, 25]]
"""