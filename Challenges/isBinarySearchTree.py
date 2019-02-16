#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isBinarySearchTree(tree):
    last = float('-inf')
    for i in in_order(tree):
        if i <= last:
            return False
        last = i
    return True

def in_order(root):
    if root:
        yield from in_order(root.left)
        yield root.value
        yield from in_order(root.right)



"""
Recently on the livestream we've been exploring the concept of a Binary Search Tree (BST) - a fun and interesting
data structure with the following properties:

It's a tree, so it's a connected graph of nodes with no loops or cycles.
Since it's a binary tree, each node has (at most) two children (this.left and this.right point to these children).
Each node also has a value (in this case, this.value is an integer), and what specifically makes it a BST is the
fact that for any given node, the left subtree contains only values less than the current node, while the right
subtree only contains values greater than the current node.
These are really useful data structures for when you need to keep an extensible list of values that's always ordered,
so they're worth knowing about! The first step is to be able to recognize a BST,
so that's what this challenge is all about!

Given tree, a binary tree, your task is to determine whether or not
it's a BST (return true if it is, or false if it isn't).

Example

For

{
    "value": 5,
    "left": {
        "value": 3,
        "left": {
            "value": 2,
            "left": null,
            "right": null
        },
        "right": null
    },
    "right": {
        "value": 8,
        "left": {
            "value": 6,
            "left": null,
            "right": null
        },
        "right": {
            "value": 9,
            "left": null,
            "right": null
        }
    }
}
the output should be isBinarySearchTree(tree) = true.

example 1

This tree has all the properties of a BST; for every node, the left subtree only contains lesser values and the
right subtree only contains greater values.

For

{
    "value": 9,
    "left": {
        "value": 8,
        "left": {
            "value": 2,
            "left": null,
            "right": null
        },
        "right": {
            "value": 6,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 5,
        "left": null,
        "right": null
    }
}
the output should be isBinarySearchTree(tree) = false.

example 2

This is a binary tree, but not a BST, since some nodes have lesser values in a right subtree.
The in-order traversal would visit the nodes in the order 2, 8, 6, 9, 5, which is not in strictly increasing order!

For

{
    "value": 1,
    "left": null,
    "right": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": {
                "value": 4,
                "left": null,
                "right": null
            }
        }
    }
}
the output should be isBinarySearchTree(tree) = true.

example 3

This tree also happens to be a linked list, but it maintains the BST property (the in-order traversal will visit
the values in strictly increasing order).
"""