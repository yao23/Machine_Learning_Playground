# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode

        @param {ListNode} head
        @param {integer} val
        @return {ListNode}

        beats 62.13%
        """
        dummy = ListNode(-1)
        dummy.next = head
        next_node = dummy

        while next_node is not None and next_node.next is not None:
            if next_node.next.val == val:
                next_node.next = next_node.next.next
            else:
                next_node = next_node.next

        return dummy.next
