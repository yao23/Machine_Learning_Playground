class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool

        beats 79.81%
        """
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
            self.isValidBST(root.right, lessThan, max(root.val, largerThan))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0098-validate-binary-search-tree.py
        
        beats 41.76%
        """
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        beats 13.52%
        """
        def dfs(node, minVal, maxVal):
            if not node:
                return True
            if node.val > minVal and node.val < maxVal:
                return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)
            else:
                return False
        return dfs(root, -sys.maxsize - 1, sys.maxsize)
