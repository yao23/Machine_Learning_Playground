"""
I: root, D
O: # of pair of leave nodes distance is less or equal to D


     1
   /  \
 2      3
/  \   / \
4   5  6  7


I: root=1, D = 2
O: 2 ([4,5], [6,7])


brute force idea: go from root to every leave node, can get its distance, calculate distance sum with every pair of leave nodes, increase counter if distance is less or equal to D


step1: find every leave node
step2: find distance between every pair of leave nodes
step3: calculate distance and compare with D (update counter accordingly)

optimized: return min(leftSubTreeHeight, rightSubTreeHeight) to parent node and process recursively
"""

class Solution:
    """
    https://www.youtube.com/watch?v=3JU0v2kuYGg
    
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

"""
brute force solution below
"""
def getLeaveNodes(root):
   nodes = []
   return nodes
  
def getLeaveNodesPairDistance(nodes):
   distance = []
   return distance
  
def getRequiredDistance(distances, D):
   counter = 0
   return counter


def solution(root):
   counter = 0
  
   leaveNodes = getLeaveNodes(root)
  
   distancecs = getLeaveNodesPairDistance(leaveNodes)
  
   counter = getRequiredDistance(distancecs)
  
   return counter

