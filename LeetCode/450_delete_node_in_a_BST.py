# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        https://www.youtube.com/watch?v=LFzAoJJt92M
        
        beats 51.10%
        """
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            cur = root.right
            while cur.left: # find smallest in right tree
                cur = cur.left
            root.val = cur.val # put smallest to the deleted position
            root.right = self.deleteNode(root.right, root.val) # recursively delete the smallest
        return root
