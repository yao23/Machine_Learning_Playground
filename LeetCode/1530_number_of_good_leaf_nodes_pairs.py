# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    https://www.youtube.com/watch?v=3JU0v2kuYGg

    T: O(n^2) - two level for loop to calculate distance
    S: O(n) - list to store left and right leave tree node distances
    
    beats 89.68%
    """
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0

        self.postorderTraversal(root, distance)

        return self.count

    """
    return a list containing root to its leave nodes distance
       1
      /\
      2 3
     /\ /\
    4 5 6 7

    4 and 5 return [1] to 2 which has [1, 1] 
    2 return 1 + each element in [1, 1] to 1 which has [2, 2] in left tree
    
    6 and 7 return [1] to 3 which has [1, 1] 
    3 return 1 + each element in [1, 1] to 1 which has [2, 2] in right tree
    
    go through left tree distances [2,2] and right tree distances [2,2] for node 1
    """
    def postorderTraversal(self, root, distance):
        if not root:
            return []

        if not root.left and not root.right: # no leave node
            return [1]

        leftDists = self.postorderTraversal(root.left, distance)
        rightDists = self.postorderTraversal(root.right, distance)

        for leftDist in leftDists:
            if leftDist >= distance:
                continue
            
            for rightDist in rightDists:
                if leftDist + rightDist <= distance:
                    self.count += 1

        # combine left and right leave nodes distances, plus one (root itself)
        return [1 + dist for dist in leftDists + rightDists]
