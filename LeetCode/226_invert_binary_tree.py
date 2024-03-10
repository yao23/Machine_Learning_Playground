# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        :type root: TreeNode
        :rtype: TreeNode

        beats 97.08%
        """
        if not root:
            return root
        
        def dfs(node):
            if not node:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            node.left = right
            node.right = left
            return node
        
        return dfs(root)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0226-invert-binary-tree.py        
        """
        if not root:
            return None
        
        # swap the children
        root.left, root.right = root.right, root.left
        
        # make 2 recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
    def invertTreeV0(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        beats 13.40%
        """
        if root:
            invert = self.invertTree
            root.left, root.right = invert(root.right), invert(root.left)
            return root
