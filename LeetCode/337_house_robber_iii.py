# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int

        beats 17.80%
        """
        return self.robDFS(root)[1]

    def robDFS(self,node):
        if node is None:
            return (0, 0)
        l = self.robDFS(node.left)
        r = self.robDFS(node.right)
        return l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val)
