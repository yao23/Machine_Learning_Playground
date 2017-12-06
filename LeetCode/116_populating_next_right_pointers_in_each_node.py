# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    # beats 90.89%
    def connect(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next