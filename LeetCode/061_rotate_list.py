# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        https://www.youtube.com/watch?v=UcGtPs2LE_c&list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB&index=14
        
        beats 56.94%
        """
        if not head or not head.next or k == 0:
            return head
        cnt = 1
        cur = head.next
        while cur:
            cnt += 1
            cur = cur.next
        n = cnt - (k % cnt)
        if n == cnt: # no rotation need
            return head
        
        pre = None
        cur = head
        while n > 0: # move the break point
            n -= 1
            pre = cur
            cur = cur.next
        pre.next = None # break 1st and 2nd half
        res = cur # record new head

        while cur and cur.next: # move to end of 2nd half
            cur = cur.next
        cur.next = head # connect to old head
        return res
        
    def rotateRightV0(self, head, k):
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

        rotate_times = k % length

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
