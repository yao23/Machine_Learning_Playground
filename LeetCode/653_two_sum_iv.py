# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # iterative
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # beats 69.48%
        if not root:
            return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False

    # recursive
    def findTarget1(self, root, k):
        # beats 51.24%
        a = set()
        self.f = False

        def dfs(root, k):
            if not root:
                return
            if root.val not in a:
                a.add(k - root.val)
                dfs(root.left, k)
                dfs(root.right, k)
            else:
                self.f = True
                return

        dfs(root, k)
        return self.f

