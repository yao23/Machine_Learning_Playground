class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    """
    https://www.youtube.com/watch?v=Wf4QhpdVFQo
    
    beats 66.63%
    """
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.tail and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        cur, prev, next = ListNode(val), self.head, self.head.next
        cur.next, cur.prev = next, prev
        next.prev = cur
        prev.next = cur

    def addAtTail(self, val: int) -> None:
        cur, prev, next = ListNode(val), self.tail.prev, self.tail
        cur.next, cur.prev = next, prev
        next.prev = cur
        prev.next = cur

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.head.next
        while next and index > 0:
            next = next.next
            index -= 1
        if next and index == 0:
            cur, prev = ListNode(val), next.prev
            cur.next, cur.prev = next, prev
            next.prev = cur
            prev.next = cur

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.tail and index == 0:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
