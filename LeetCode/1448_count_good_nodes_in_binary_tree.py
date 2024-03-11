# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Beats 87.39%
        """
        res = 0
        def dfs(node, m):
            nonlocal res
            if not node:
                return
            if node.val >= m:
                res += 1
                m = node.val
            dfs(node.left, m)
            dfs(node.right, m)

        if not root:
            return 0
        dfs(root, root.val)
        return res

    def goodNodes(self, root: TreeNode) -> int:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/1448-count-good-nodes-in-binary-tree.py

        Beats 61.52%
        """
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
