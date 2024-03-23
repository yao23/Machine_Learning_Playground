# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Iterative
        beats 94.04%
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Recursive
        beats 29.29%
        """
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        https://www.youtube.com/watch?v=G0_I-ZF0S38&list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB&index=2
        
        beats 38.62%
        """
        if head is None or head.next is None:
            return head
        return self.reverse_helper(None, head)

    def reverse_helper(self, prev, current):
        if current.next is None:
            return current
        res = self.reverse_helper(current, current.next)
        current.next.next = current
        current.next = prev
        return res
