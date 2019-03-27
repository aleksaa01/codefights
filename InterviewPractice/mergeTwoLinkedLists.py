# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 or l2:
        if l1 is None:
            cur.next = l2
            break
        elif l2 is None:
            cur.next = l1
            break

        v1 = l1.value
        v2 = l2.value

        if v1 <= v2:
            cur.next = ListNode(v1)
            cur = cur.next
            l1 = l1.next
        else:
            cur.next = ListNode(v2)
            cur = cur.next
            l2 = l2.next

    return dummy.next





"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a 
singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
"""