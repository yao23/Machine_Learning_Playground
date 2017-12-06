# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # beats 51.72%
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):  # returns: max one side path sum, max path sum
            l = r = 0
            ls = rs = None
            if node.left:
                l, ls = dfs(node.left)
                l = max(l, 0)
            if node.right:
                r, rs = dfs(node.right)
                r = max(r, 0)
            return node.val + max(l, r), max(node.val + l + r, ls, rs)
        if root:
            return dfs(root)[1]
        return 0