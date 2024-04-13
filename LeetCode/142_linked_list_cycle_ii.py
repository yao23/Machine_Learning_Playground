# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        beats 88.06%
        """
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break

        if slow is fast:
            slow2 = head
            while slow2 is not slow:
                slow2 = slow2.next
                slow = slow.next
            return slow
        else:
            return None
            
    def detectCycleV0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        beats 55.64%
        """
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head
