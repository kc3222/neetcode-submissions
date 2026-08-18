class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dct = defaultdict(list)
        for edge in edges:
            dct[edge[0]].append(edge[1])
            dct[edge[1]].append(edge[0])
        
        visited = set()

        def dfs(currentNode, lastNode):
            visited.add(currentNode)
            res = True
            connected = dct[currentNode]
            for node in connected:
                if node == lastNode:
                    continue
                elif node in visited:
                    return False
                else:
                    res = dfs(node, currentNode)
            return res
        
        return dfs(0, -1) and len(visited) == n