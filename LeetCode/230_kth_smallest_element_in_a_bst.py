# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # beats 68.74%
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count)
        return count[k - 1]

    def helper(self, node, count):
        if not node:
            return

        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)