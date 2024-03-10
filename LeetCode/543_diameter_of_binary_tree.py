# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0543-diameter-of-binary-tree.py
        
        beats 20.67%
        """
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left + right > res:
                res = left + right
            return 1 + max(left, right)

        dfs(root)
        return res

