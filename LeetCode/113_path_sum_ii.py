# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # beats 39.96%
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)

    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in tmp]

    # BFS + queue
    def pathSum3(self, root, sum):
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val + curr.left.val, ls + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, val + curr.right.val, ls + [curr.right.val]))
        return res

    # DFS + stack I
    def pathSum4(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
        return res

        # DFS + stack II

    def pathSum5(self, root, s):
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls + [curr.left.val]))
        return res