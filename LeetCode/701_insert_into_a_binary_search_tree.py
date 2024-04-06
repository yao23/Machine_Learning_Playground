# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        https://www.youtube.com/watch?v=Cpg8f79luEA

        recursive
        
        beats 28.53%
        """
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def insertIntoBSTV0(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        https://www.youtube.com/watch?v=Cpg8f79luEA
        
        iterative 
        
        beats 98.91%
        """
        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
