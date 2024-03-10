class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int

        beats 90.44%
        """
        res = 0

        def dfs(node, depth):
            nonlocal res
            if not node:
                return

            depth += 1
            if not node.left and not node.right:
                if depth > res:
                    res = depth

            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)
        return res

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        beats 10.60%
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0104-maximum-depth-of-binary-tree.py
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ITERATIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
