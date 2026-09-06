class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find
        parents = [i for i in range(len(edges) + 1)]

        def findParent(x):
            while parents[x] != x:
                x = parents[x]
            return x

        def union(x, y):
            parentX = findParent(x)
            parentY = findParent(y)
            if parentX == parentY:
                return False # Already union
            parents[parentY] = parents[parentX]
            return True
        
        res = None
        for edge in edges:
            unionXY = union(edge[0], edge[1])
            if not unionXY:
                res = edge
        return res