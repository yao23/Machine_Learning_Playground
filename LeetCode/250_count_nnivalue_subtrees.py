# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # beats 86.26%
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.checkUni(root)
        return self.count

    # bottom-up, first check the leaf nodes and count them,
    # then go up, if both children are "True" and root.val is
    # equal to both children's values if exist, then root node
    # is uniValue suntree node.
    def checkUni(self, root):
        if not root:
            return True
        l, r = self.checkUni(root.left), self.checkUni(root.right)
        if l and r and (not root.left or root.left.val == root.val) and \
                (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False
