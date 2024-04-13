# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        """
        https://www.youtube.com/watch?v=gBTe7lFR3vc
        
        beats 89.53%
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
    def hasCycleV1(self, head):
        """
        :type head: ListNode
        :rtype: bool

        beats 40.62%
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

    def hasCycleV0(self, head: Optional[ListNode]) -> bool:
        """
        beats 22.84%
        """
        if not head or not head.next:
            return False
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
