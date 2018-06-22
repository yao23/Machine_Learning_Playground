# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        beats 13.40%
        """
        if root:
            invert = self.invertTree
            root.left, root.right = invert(root.right), invert(root.left)
            return root
