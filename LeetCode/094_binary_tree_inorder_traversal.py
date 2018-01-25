# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Recursive

        beats 26.66%
        """
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Iterative

        in-order traversal needs to start from left child, and process current node if there is no left child
        it needs a data structure to store visiting trace and check last one when necessary, so stack is ideal
        after finish processing left and current ones, start deal with right sub-tree

        beats 99.08%
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
