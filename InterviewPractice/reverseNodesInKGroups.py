# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    if k == 1:
        return l
    new_head = None

    count = 0
    head = None
    tail = None
    head_parent = None
    prev_node = None
    while l:
        count += 1
        if count == 1:
            head = l
            head_parent = prev_node
        elif count == k:
            tail = l
            l = reverse_nodes(head, tail, head_parent, k)
            if head_parent is None:
                new_head = tail
            count = 0
        prev_node = l
        l = l.next
    return new_head


def reverse_nodes(head, tail, head_parent, num_nodes):
    new_end_parent = tail.next
    count = 0
    parent = tail.next
    temp_child = None
    cur = head
    while count < num_nodes:
        count += 1
        temp_child = cur.next
        cur.next = parent
        parent = cur
        cur = temp_child
    if head_parent:
        head_parent.next = parent

    return head




"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space 
complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less 
than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that 
are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
"""