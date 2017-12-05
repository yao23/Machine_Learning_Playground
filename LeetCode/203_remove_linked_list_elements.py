# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #beats 62.13%
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy

        while next != None and next.next != None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next

        return dummy.next