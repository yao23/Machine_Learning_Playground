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
