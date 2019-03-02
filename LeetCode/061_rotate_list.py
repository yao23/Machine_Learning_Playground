# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        beats 62.24%
        """
        if not head:
            return None

        if head.next is None:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1

        rotate_times = k%length

        if k == 0 or rotate_times == 0:
            return head

        fast_pointer = head
        slow_pointer = head

        for a in range (rotate_times):
            fast_pointer = fast_pointer.next

        while fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        temp = slow_pointer.next

        slow_pointer.next = None
        fast_pointer.next = head
        head = temp

        return head
