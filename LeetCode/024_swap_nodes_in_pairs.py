# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        https://www.youtube.com/watch?v=o811TZLAWOo&list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB&index=9
        
        beats 73.14%
        """
        if not head or not head.next:
            return head
        dummy = ListNode(next=head.next)
        pre = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next
            tmp = nxt.next

            # swap first and second node
            pre.next = nxt
            nxt.next = cur
            cur.next = tmp

            pre = cur
            cur = tmp

        return dummy.next
        
    def swapPairsV0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        beats 90.86%
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
