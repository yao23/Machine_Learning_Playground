# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param node, a undirected graph node
    @return a undirected graph node
    beats 92.16%
    """
    def cloneGraph(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        stack = [node]
        visit = {node.label: root}  # map original node to new one
        while stack:
            top = stack.pop()

            for n in top.neighbors:
                if n.label not in visit:
                    stack.append(n)
                    visit[n.label] = UndirectedGraphNode(n.label)  # map original node neighbor to new one
                visit[top.label].neighbors.append(visit[n.label])

        return root
