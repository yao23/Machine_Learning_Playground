# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        tmpHead = ListNode(0)
        cur = tmpHead
        head1, head2 = list1, list2
        while head1 and head2:
            if head1.val < head2.val:
                tmp = head1.next
                cur.next = head1
                head1.next = None
                cur = head1
                head1 = tmp
            else:
                tmp = head2.next
                cur.next = head2
                head2.next = None
                cur = head2
                head2 = tmp
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return tmpHead.next
