class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        beats 43.37%
        """
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans

    def levelOrder1(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans

    def levelOrder2(self, root):
        """
        Beats 46.41%
        """
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans

    def levelOrder3(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Beats 37.03% of users with Python3
        """
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        visit = set()
        while q:
            size = len(q)
            tmp = []
            for _ in range(size):
                cur = q.popleft()
                tmp.append(cur.val)
                visit.add(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(tmp)
        return res

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0102-binary-tree-level-order-traversal.py
        """
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
