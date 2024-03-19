# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        https://www.youtube.com/watch?v=U4hFQCa1Cq0&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=34
        
        beats 97.11%
        """
        cur, nxt = root, root.left if root else None

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur: # no next 
                cur = nxt
                nxt = cur.left
        return root
        
    def connect0(self, root):
        """
        :param root:
        :return:

        @param root, a tree link node
        @return nothing
        beats 90.89%
        """
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
