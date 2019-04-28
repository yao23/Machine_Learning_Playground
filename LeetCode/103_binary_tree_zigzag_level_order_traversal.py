class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        beats 47.51%
        """
        if not root:
            return []
        res, temp, stack, flag = [], [], [root], 1
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                temp += [node.val]
                if node.left:
                    stack += [node.left]
                if node.right:
                    stack += [node.right]
            res += [temp[::flag]]
            temp = []
            flag *= -1
        return res
