# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    """
    https://www.youtube.com/watch?v=RXy5RzGF5wo&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=33
    
    beats 77.41%
    """
    def __init__(self, root: Optional[TreeNode]):
        self.stack = [] # store in-order traversed nodes 
        cur = root
        while cur: # find smallest and push all nodes on the way to stack
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        res = self.stack.pop() # stack top element is smallest
        cur = res.right # find smallest one in right tree
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return self.stack != []

class BSTIterator0(object):
    def __init__(self, root):
        """
        :type root: TreeNode

        @param root, a binary search tree's root node
        beats 28.34%
        """
        self.stack = list()
        self.pushAll(root)

    def hasNext(self):
        """
        :rtype: bool

        @return a boolean, whether we have a next smallest number
        """
        return self.stack

    def next(self):
        """
        :rtype: int

        @return an integer, the next smallest number
        """
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
