# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
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
