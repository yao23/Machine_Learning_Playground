# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # beats 97.40%
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        tree_list = [[[None]] * (n + 2) for _ in range(n + 2)]
        for i in range(1, n + 1):
            tree_list[i][i] = [TreeNode(i)]
            for j in reversed(range(1, i)):
                tree_list[j][i] = []
                for k in range(j, i + 1):
                    for left in tree_list[j][k - 1]:
                        for right in tree_list[k + 1][i]:
                            root = TreeNode(k)
                            (root.left, root.right) = (left, right)
                            tree_list[j][i].append(root)
        return tree_list[1][n]

    def generateTrees1(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n + 1)

    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    result.append(node)
        return result

    def generateTrees2(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]

        beats 37.50%
        """

        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node

        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last + 1)
                    for left in trees(first, root - 1)
                    for right in trees(root + 1, last)] or [None]

        if n == 0:
            return []
        else:
            return trees(1, n)

    def generateTrees4(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]

        beats 53.13%
        """

        def generate(first, last):
            trees = []
            for root in range(first, last + 1):
                for left in generate(first, root - 1):
                    for right in generate(root + 1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            return trees or [None]

        if n == 0:
            return []
        else:
            return generate(1, n)
