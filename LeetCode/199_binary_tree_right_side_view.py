# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Recursive, combine right and left
        Compute the right view of both right and left left subtree,
        then combine them. For very unbalanced trees, this can be O(n^2), though.
        beats 79.79%
        """
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]

    def rightSideView1(self, root):
        """
        :param root:
        :return:

        Recursive, first come first serve
        DFS-traverse the tree right-to-left,
        add values to the view whenever we first reach a new record depth. This is O(n).
        """
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(root, 0)
        return view

    def rightSideView2(self, root):
        """
        :param root:
        :return:

        Iterative, level-by-level
        Traverse the tree level by level and add the last value of each level to the view. This is O(n).
        """
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view
