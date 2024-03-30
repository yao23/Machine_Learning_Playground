# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        https://www.youtube.com/watch?v=Jk16lZGFWxE&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=8

        FB
        
        beats 40.01%
        """
        res = 0

        def dfs(root, tmp):
            nonlocal res
            if not root:
                return
            if not root.left and not root.right:
                res += int(tmp + str(root.val))
                return
            
            dfs(root.left, tmp + str(root.val))
            dfs(root.right, tmp + str(root.val))

        dfs(root, "")
        return res
        
    def sumNumbers0(self, root):
        """
        :type root: TreeNode
        :rtype: int

        recursively
        beats 30.29%
        """
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            # if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.left, value*10+root.val)
            # if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val

    def sumNumbers1(self, root):
        """
        :param root:
        :return:

        dfs + stack
        """
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value * 10 + node.right.val))
                if node.left:
                    stack.append((node.left, value * 10 + node.left.val))
        return res

    def sumNumbers2(self, root):
        """
        :param root:
        :return:

        bfs + queue
        """
        if not root:
            return 0
        queue, res = collections.deque([(root, root.val)]), 0
        while queue:
            node, value = queue.popleft()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.left:
                    queue.append((node.left, value * 10 + node.left.val))
                if node.right:
                    queue.append((node.right, value * 10 + node.right.val))
        return res
