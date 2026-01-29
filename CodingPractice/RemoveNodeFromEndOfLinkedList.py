# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode()
        tmp.next = head
        pre = tmp
        p1 = p2 = head
        while n and p2:
            p2 = p2.next
            n -= 1
        
        while p2:
            pre = p1
            p1 = p1.next
            p2 = p2.next
        pre.next = p1.next
        p1.next = None
        return tmp.next
