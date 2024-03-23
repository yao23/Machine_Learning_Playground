from Queue import PriorityQueue


class ListNode(object):
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        https://www.youtube.com/watch?v=q5a5OiGbT6Q&list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB&index=6
        
        beats 97.87%
        """
        if not lists or len(lists) == 0:
            return None
        
        def mergeList(l1, l2): # merge 2 lists
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next 
                else:
                    tail.next = l2
                    l2 = l2.next 
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeKListsV0(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        beats 32.93%
        """
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next
