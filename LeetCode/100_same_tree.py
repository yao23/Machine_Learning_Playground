class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Beats 97.55%
        """
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False
            
    def isSameTree0(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool

        beats 25.98%
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0100-same-tree.py
        """
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
            
    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool

        beats 47.51%
        """

        def t(n):
            return n and (n.val, t(n.left), t(n.right))

        return t(p) == t(q)

    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool

        beats 32.56%
        """
        return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q
