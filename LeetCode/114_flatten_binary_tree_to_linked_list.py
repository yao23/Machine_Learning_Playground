# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    # beats 75.80%
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        '''
        1. flatten left subtree
        2. find left subtree's tail
        3. set root's left to None, root's right to root'left, tail's right to root.right
        4. flatten the original right subtree
        '''
        # escape condition
        if not root:
            return
        right = root.right
        if root.left:
            # flatten left subtree
            self.flatten(root.left)
            # find the tail of left subtree
            tail = root.left
            while tail.right:
                tail = tail.right
            # left <-- None, right <-- left, tail's right <- right
            root.left, root.right, tail.right = None, root.left, right
        # flatten right subtree
        self.flatten(right)