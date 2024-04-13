# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        https://www.youtube.com/watch?v=doj95MelfSA

        beats 96.03%
        """
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev # reverse next pointer in left half
            prev = slow
            slow = tmp
        
        res = 0
        while slow:
            res = max(res, prev.val + slow.val) # twin sum
            prev = prev.next
            slow = slow.next

        return res
