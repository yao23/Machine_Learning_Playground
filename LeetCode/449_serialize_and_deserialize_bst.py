# Definition for a binary tree node.
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
