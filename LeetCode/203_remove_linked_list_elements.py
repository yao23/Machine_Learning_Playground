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

    def removeElementsV1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        https://www.youtube.com/watch?v=JI71sxtHTng&list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB&index=3
        
        beats 94.14%
        """
        node = ListNode(next=head)
        pre, cur = node, head

        while cur:
            nxt = cur.next
            if cur.val == val:
                pre.next = nxt
            else:
                pre = cur
            cur = nxt

        return node.next
        
    def removeElementsV0(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        beats 75.62%
        """
        node = ListNode(0)
        node.next = head
        pre = node

        while head:
            while head and head.val == val:
                nxt = head.next
                head.next = None
                head = nxt
            pre.next = head
            pre = head
            if head:
                head = head.next

        return node.next
