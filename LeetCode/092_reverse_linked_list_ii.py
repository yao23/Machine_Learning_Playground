class ListNode(object):
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode

        # The idea is simple and intuitive: find linkedlist [m, n], reverse it,
        # then connect m with n+1, connect n with m-1
        # @param head, a ListNode
        # @param m, an integer
        # @param n, an integer
        # @return a ListNode
        # input: 1->2->3->4->5, m = 2, n = 4, return 1->4->3->2->5
        # beats 43.68%
        """
        if m == n:
            return head

        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node

        for i in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes, [2, 3, 4] in example
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next_node = cur.next
            cur.next = reverse
            reverse = cur
            cur = next_node

        pre.next.next = cur  # connect m with n+1, 2->5 in example output (pre = 1, pre.next = 2, cur = 5)
        pre.next = reverse  # connect n with m-1, 1->4 in example output (reverse = 4)

        return dummy_node.next
