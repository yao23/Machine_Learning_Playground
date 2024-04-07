class LinkedNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int

        https://discuss.leetcode.com/topic/14591/python-dict-double-linkedlist/5
        beats 73.27%
        """
        self.capacity = capacity
        self.head = LinkedNode(None, 'head')
        self.tail = LinkedNode(None, 'tail')
        self.head.next = self.tail  # tail being most recent
        self.tail.prev = self.head  # head being oldest
        self.data = {}

    def deleteNode(self, node):
        assert (node is not self.head and node is not self.tail)
        del self.data[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def get(self, key):
        if key not in self.data:
            return -1
        node = self.data[key]
        # take the node out
        node.prev.next = node.next
        node.next.prev = node.prev
        # insert into most recent position
        self.insertNew(node)
        return node.value

    def put(self, key, value):
        # remove old value if present
        if key in self.data:
            self.deleteNode(self.data[key])

        # create new node
        new_node = LinkedNode(key, value)
        self.data[key] = new_node

        # if over limit, delete oldest node
        if len(self.data) > self.capacity:
            self.deleteNode(self.head.next)

        self.insertNew(new_node)

    def insertNew(self, newNode):
        # insert new node into last position
        last = self.tail.prev
        last.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = last


# https://www.youtube.com/watch?v=7ABFKPK2hD4
# TikTok / Microsoft
# beats 53.57%

class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            node = self.removeFromList(key)
            self.addToHead(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.count == self.capacity:
                self.count -=1
                tmp = self.removeFromList(self.tail.prev.key)
                del self.map[tmp.key]

            node = ListNode(key, value)
            self.addToHead(node)
            self.count += 1
            self.map[key] = node
        else:
            node = self.removeFromList(key)
            self.addToHead(node)
            node.val = value

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head   
        self.head.next.prev = node
        self.head.next = node

    def removeFromList(self, key):
        node = self.map[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
