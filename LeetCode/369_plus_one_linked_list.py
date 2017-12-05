# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # beats 43.57%
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = None

        node = head
        while node:
            if node.val < 9:
                start = node
            node = node.next

        if start:
            start.val += 1
            node = start.next
        else:
            new = ListNode(1)
            new.next = head
            node = head
            head = new

        while node:
            node.val = 0
            node = node.next

        return head