# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        https://discuss.leetcode.com/topic/80043/concise-iterative-python-solution-using-stack-beat-99/3
        utilize BST feature (if-else block in deserialize() function)

        beats 93.27%
        """
        res = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        return ' '.join(map(str, res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        stack = []
        data_arr = map(int, data.split())
        if len(data_arr) == 0:
            return None
        root = TreeNode(data_arr[0])
        cur = root

        for value in data_arr[1:]:
            if value < cur.val:
                cur.left = TreeNode(value)
                stack.append(cur)
                cur = cur.left
            else:
                while stack and stack[-1].val < value:
                    cur = stack.pop()

                cur.right = TreeNode(value)
                cur = cur.right

        return root


class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93171/

        beats 95.29%
        """
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = collections.deque(int(val) for val in data.split())

        def build(min_val, max_val):
            if values and min_val < values[0] < max_val:
                val = values.popleft()
                node = TreeNode(val)
                node.left = build(min_val, val)
                node.right = build(val, max_val)
                return node

        return build(float('-infinity'), float('infinity'))


class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        beats 52.86%
        """
        res = ""
        if root:
            res += (str(root.val) + " ")
            res += (self.serialize(root.left) + " ")
            res += (self.serialize(root.right) + " ")
            return res
        else:
            return "#"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def build_tree(values):
            val = next(values)
            if val == '#':
                return None
            else:
                root = TreeNode(val)
                root.left = build_tree(values)
                root.right = build_tree(values)
                return root

        values = iter(data.split())
        return build_tree(values)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
