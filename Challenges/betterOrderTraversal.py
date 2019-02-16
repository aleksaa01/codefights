#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def betterOrderTraversal(root):
    first = [i for i in in_order(root)]
    second = [i for i in pre_order(root)]
    third = [i for i in post_order(root)]

    return min(first, second, third)


def in_order(root):
    if root:
        yield from in_order(root.left)
        yield root.value
        yield from in_order(root.right)


def pre_order(root):
    if root:
        yield root.value
        yield from pre_order(root.left)
        yield from pre_order(root.right)


def post_order(root):
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.value


"""
There are several ways to traverse a binary tree. Let's talk about some of the most popular ways!

In-order traversal involves looking at the left subtree, then the current node, then the right subtree.
This will visit the values of a binary search tree in ascending order.

Pre-order traversal involves looking at the current node, then the left subtree, then the right subtree.
This type of traversal is often used for copying a tree.

Post-order traversal involves looking at the left subtree, then the right subtree, then the current node.
This type of traversal is often used for deleting a tree.

Given a binary tree, your task is to test each of these traversals - store the values in an array
(in the order in which they're visited), and return the one that's lexicographically smallest.

Example

For

{
    "value": -29,
    "left": {
        "value": 95,
        "left": null,
        "right": null
    },
    "right": {
        "value": 2,
        "left": null,
        "right": {
            "value": 100,
            "left": null,
            "right": null
        }
    }
}
the output should be betterOrderTraversal(root) = [-29, 95, 2, 100]

example

The different traversal types would visit the nodes in the following orders:

In-order: [95, -29, 2, 100]
Pre-order: [-29, 95, 2, 100]
Post-order: [95, 100, 2, -29]
So in this case, pre-order traversal produces the lexicographically smallest result.
"""