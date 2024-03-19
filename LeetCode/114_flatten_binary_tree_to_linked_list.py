# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        https://www.youtube.com/watch?v=rKnD7rLT0lI&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=25
        
        beats 60.66%
        """
        def dfs(root):
            if not root:
                return None
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            last = rightTail or leftTail or root
            return last
        dfs(root)
        
    def flatten0(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        1. flatten left subtree
        2. find left subtree's tail
        3. set root's left to None, root's right to root'left, tail's right to root.right
        4. flatten the original right subtree

        beats 75.80%
        """
        # escape condition
        if not root:
            return
        right = root.right
        if root.left:
            # flatten left subtree
            self.flatten(root.left)
            # find the tail of left subtree
            tail = root.left
            while tail.right:
                tail = tail.right
            # left <-- None, right <-- left, tail's right <- right
            root.left, root.right, tail.right = None, root.left, right
        # flatten right subtree
        self.flatten(right)

    prev = None

    def flatten1(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        beats 44.12%
        """
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
