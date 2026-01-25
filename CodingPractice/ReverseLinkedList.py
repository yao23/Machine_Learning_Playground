# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        next = head.next
        head.next = None
        return self.reverse(head, next)

    def reverse(self, cur, next):
        if next == None:
            return cur
        tmp = next.next
        next.next = cur
        return self.reverse(next, tmp)
