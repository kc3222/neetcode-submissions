"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dct of nodes
        # Connect neighbors after
        if not node:
            return
        visited = {} # original: cloned
        
        def dfs(node, visited):
            if node in visited:
                return visited[node]
            clonedNode = Node(val = node.val)
            visited[node] = clonedNode
            clonedNeighbors = []
            for neighbor in node.neighbors:
                clonedNeighbors.append(dfs(neighbor, visited))
            clonedNode.neighbors = clonedNeighbors
            return clonedNode
        
        newNode = dfs(node, visited)
        return newNode
        