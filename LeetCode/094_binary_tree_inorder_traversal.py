# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Recursive

        beats 26.66%
        """
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Iterative

        in-order traversal needs to start from left child, and process current node if there is no left child
        it needs a data structure to store visiting trace and check last one when necessary, so stack is ideal
        after finish processing left and current ones, start deal with right sub-tree

        beats 99.08%
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def inorderTraversal2(self, root):
        """
        :param root:
        :return:

        beats 45.21%
        """
        class OpsElement:
            def __init__(self, ops, element):
                self.__ops = ops
                self.__element = element

            def get_ops(self):
                return self.__ops

            def get_element(self):
                return self.__element

        res = []
        stack = list()
        stack.append(OpsElement(0, root))
        while stack:
            cur_ops_element = stack.pop()
            if cur_ops_element.get_element() is None:
                continue
            if cur_ops_element.get_ops() == 0:  # visit
                stack.append(OpsElement(0, cur_ops_element.get_element().right))
                stack.append(OpsElement(1, cur_ops_element.get_element()))
                stack.append(OpsElement(0, cur_ops_element.get_element().left))
            else:  # print
                res.append(cur_ops_element.get_element().val)
        return res
