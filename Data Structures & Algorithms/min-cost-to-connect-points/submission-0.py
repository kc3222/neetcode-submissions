class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Krusal algo + Union Find
        numPoints = len(points)
        parent = [i for i in range(numPoints)]

        def findParent(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def unionFind(x, y):
            parentX = findParent(x)
            parentY = findParent(y)
            return parentX != parentY
        
        def union(x, y):
            parentX = findParent(x)
            parentY = findParent(y)
            parent[parentY] = parent[parentX]
        
        allEdges = []
        for i in range(numPoints - 1):
            for j in range(i + 1, numPoints):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                allEdges.append((dist, i, j))
        allEdges = sorted(allEdges, key = lambda x: x[0])
        
        # Calculate
        res = 0
        numEdges = 0
        for i in range(len(allEdges)):
            if numEdges == numPoints - 1:
                break
            edge, v1, v2 = allEdges[i]
            if unionFind(v1, v2):
                union(v1, v2)
                res += edge
                numEdges += 1

        return res