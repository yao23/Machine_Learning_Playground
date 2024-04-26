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

