# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]

        beats 60.27%
        """

        # Helper, takes a path and makes it the path to the next node
        def nextpath(path, kid1, kid2):
            if path:
                if kid2(path):
                    path += kid2(path),
                    while kid1(path):
                        path += kid1(path),
                else:
                    kid = path.pop()
                    while path and kid is kid2(path):
                        kid = path.pop()

        # These customize nextpath as forward or backward iterator
        kidleft = lambda path: path[-1].left
        kidright = lambda path: path[-1].right

        # Build path to closest node
        path = []
        while root:
            path += root,
            root = root.left if target < root.val else root.right
        dist = lambda node: abs(node.val - target)
        path = path[:path.index(min(path, key=dist)) + 1]

        # Get the path to the next larger node
        path2 = path[:]
        nextpath(path2, kidleft, kidright)

        # Collect the closest k values by moving the two paths outwards
        vals = []
        for _ in range(k):
            if not path2 or path and dist(path[-1]) < dist(path2[-1]):
                vals += path[-1].val,
                nextpath(path, kidright, kidleft)
            else:
                vals += path2[-1].val,
                nextpath(path2, kidleft, kidright)
        return vals
