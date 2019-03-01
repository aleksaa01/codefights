# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    slow_p = l
    fast_p = l
    counter = 0
    while fast_p and fast_p.next:
        counter += 1
        fast_p = fast_p.next.next
        slow_p = slow_p.next

    middle = slow_p
    cur = middle
    if fast_p:
        cur = middle.next

    parent = None
    temp_child = None
    while cur:
        temp_child = cur.next
        cur.next = parent
        parent = cur
        cur = temp_child

    cur1 = l
    cur2 = parent
    while cur2:
        if cur1.value != cur2.value:
            return False

        cur1 = cur1.next
        cur2 = cur2.next

    return True



"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l,
since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;
For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.
"""