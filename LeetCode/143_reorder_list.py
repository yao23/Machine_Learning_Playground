# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.

        beats 40.65%
        """
        if head is None:
            return
        p = head
        q = head
        # slow pointer p and quick pointer q
        while q is not None and q.next is not None:
            q = q.next.next
            p = p.next
        # find middle
        mid = p.next
        p.next = None
        begin = head
        end = mid
        pre = None
        # reverse link
        while end is not None:
            temp = end.next
            end.next = pre
            pre = end
            end = temp
        # merge link
        while pre is not None and begin is not None:
            a = pre.next
            b = begin.next
            begin.next = pre
            pre.next = b
            begin = b
            pre = a
        return
