# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool

        Recursive
        beats 78.16%
        """
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            if left < 0:
                return left
            right = dfs(node.right)
            if right < 0:
                return right
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) >= 0
    
    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0110-balanced-binary-tree.py
        """
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
    
    def isBalanced0(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Recursive
        beats 80.21%
        """

        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

    def isBalanced1(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Iterative
        beats 97.16%
        """
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1:
                        return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
