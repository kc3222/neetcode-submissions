class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dct = defaultdict(list)
        for edge in edges:
            dct[edge[0]].append(edge[1])
            dct[edge[1]].append(edge[0])
        # Loop
        res = 0
        visited = set()

        def dfs(x):
            visited.add(x)
            for e in dct[x]:
                if e in visited:
                    continue
                else:
                    dfs(e)
            return

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res