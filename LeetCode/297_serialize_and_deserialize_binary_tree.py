class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        beats 65.22%
        """

        def doit(node):
            if node:
                values.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                values.append('#')

        values = []
        doit(root)
        return ' '.join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def doit():
            val = next(values)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        values = iter(data.split())
        return doit()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
