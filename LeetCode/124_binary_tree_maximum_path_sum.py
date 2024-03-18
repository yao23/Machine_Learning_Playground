import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        https://www.youtube.com/watch?v=Hr5cWUld4vU&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=21

        beats 77.76%
        """
        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            leftSide = node.val + left
            rightSide = node.val + right
            arc = node.val + left + right
            res = max(res, max(node.val, max(arc, max(leftSide, rightSide))))
            return max(node.val, max(leftSide, rightSide))
        
        dfs(root)
        return res
        
    def maxPathSum0(self, root):
        """
        :type root: TreeNode
        :rtype: int

        beats 51.72%
        """
        def dfs(node):  # returns: max one side path sum, max path sum
            # track "one-side" max sum
            l_max_sum = r_max_sum = 0

            # track the max path that doesn't go through the root
            # max will consider None to be the lowest value possible
            ls = rs = None
            if node.left:
                l_max_sum, ls = dfs(node.left)
                l_max_sum = max(l_max_sum, 0)
            if node.right:
                r_max_sum, rs = dfs(node.right)
                r_max_sum = max(r_max_sum, 0)
            return node.val + max(l_max_sum, r_max_sum), max(node.val + l_max_sum + r_max_sum, ls, rs)
        if root:
            return dfs(root)[1]
        return 0

    def maxPathSum1(self, root):
        Solution.max_value = -sys.maxsize - 1
        """
        :type root: TreeNode
        :rtype: int
        
        beats 38.30%
        """

        self.max_path_down(root)
        return Solution.max_value

    def max_path_down(self, node):
        if node is None:
            return 0
        left = max(0, self.max_path_down(node.left))
        right = max(0, self.max_path_down(node.right))
        Solution.max_value = max(Solution.max_value, left + right + node.val)
        return max(left, right) + node.val
