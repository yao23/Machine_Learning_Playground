# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int

        in-order traversal

        beats 68.74%
        """
        count = []
        self.helper(root, count)
        return count[k - 1]

    def helper(self, node, count):
        if not node:
            return

        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        https://github.com/neetcode-gh/leetcode/blob/main/python/0230-kth-smallest-element-in-a-bst.py
        
        beats 58.41
        """
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
