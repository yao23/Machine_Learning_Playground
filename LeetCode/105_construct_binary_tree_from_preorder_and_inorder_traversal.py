class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    Construct a binary tree from preorder and inorder traversal list
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode

        beats 67.34%
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

    def buildTree0(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        beats 9.53%
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        idx = 0 
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                idx = i
                break
        if idx == 0:
            left = None
            right = self.buildTree(preorder[1:], inorder[1:])
        else:
            left = self.buildTree(preorder[1:idx+1], inorder[:idx])
            right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        root.left = left
        root.right = right
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0105-construct-binary-tree-from-preorder-and-inorder-traversal.py
        
        beats 37.43%
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
