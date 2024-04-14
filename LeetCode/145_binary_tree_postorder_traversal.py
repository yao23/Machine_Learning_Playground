# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    https://www.youtube.com/watch?v=QhszUQhGGlA
    """
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        beats 94.77%
        """
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return traversal

    def postorderTraversal1(self, root):
        """
        :param root:
        :return:

        beats 23.73%
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
                stack.append(OpsElement(1, cur_ops_element.get_element()))
                stack.append(OpsElement(0, cur_ops_element.get_element().right))
                stack.append(OpsElement(0, cur_ops_element.get_element().left))
            else:  # print
                res.append(cur_ops_element.get_element().val)
        return res
