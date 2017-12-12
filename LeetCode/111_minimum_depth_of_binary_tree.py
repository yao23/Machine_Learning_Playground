# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # beats 24.17%
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        d = map(self.minDepth, (root.left, root.right))
        return 1 + (min(d) or max(d))  # mid(d) might be zero, but minDepth only counts root to left, e.g. 1 -> 2

    def minDepth1(self, root):
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)
