# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # beats 24.21%
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        l_root = self.upsideDownBinaryTree(root.left)
        r_most = l_root
        while r_most.right:
            r_most = r_most.right
        root = l_root
        r_most.left = root.right
        r_most.right = TreeNode(root.val)
        return root

    def upsideDownBinaryTree1(self, root):
        # beats 55.79%
        if not root or not root.left:
            return root

        parent = None
        right = None
        cur = root

        while cur:
            left = cur.left

            cur.left = right
            right = cur.right  # avoid miss (override) cur.right in next step
            cur.right = parent

            parent = cur
            cur = left

        return parent
