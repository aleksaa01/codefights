# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if l is None or n == 0:
        return l

    original_head = l
    new_head = l
    new_head_parent = None
    prev_node = None
    count = 0
    while l:
        if count == n:
            new_head_parent = new_head
            new_head = new_head.next
        elif count < n:
            count += 1
        prev_node = l
        l = l.next

    if new_head_parent is None:
        return new_head

    new_head_parent.next = None
    prev_node.next = original_head
    return new_head




"""
Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked
during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning
of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
"""