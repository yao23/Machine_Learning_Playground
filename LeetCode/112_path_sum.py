# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool

        @param root, a tree node
        @param sum, an integer
        @return a boolean
        beats 93.59%
        """
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
