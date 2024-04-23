"""
Given a binary tree and two nodes in that tree, find the lowest common ancestor of those nodes.
//     3
//    / \
//   9   7
//  / \   \
// 2   6   4

// 2, 6 -> 9
// 7, 6 -> 3
"""

# S: height of tree (o(logn)) if number of tree nodes is n, worst case is O(n) as recursion stack level is number of nodes
# T: O(n) since have to go over all nodes if this is a linked list wise and target nodes are leave nodes
def lowestCommonAncestor(root, node1, node2): #3, 2, 6
    if root is None:
        return root
    if node1 and root.val == node1.val or node2 and root.val == node2.val: 
        return root
    left = lowestCommonAncestor(root.left, node1, node2) # 2
    right = lowestCommonAncestor(root.righ, node1, node2) # 6
    if left is not None and right is not None:
        return root # 9, 3
    return left if left else right



