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

    def hasPathSumV0(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        https://www.youtube.com/watch?v=LSKQyOz_P8I
        
        beats 90.20%
        """
        if not root:
            return False
        def dfs(node, sum):
            if not node:
                return False 
            if not node.left and not node.right:
                return sum + node.val == targetSum
            return dfs(node.left, sum + node.val) or dfs(node.right, sum + node.val)
        return dfs(root, 0)
