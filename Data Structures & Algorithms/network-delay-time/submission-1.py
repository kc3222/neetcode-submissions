class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build a dictionary
        # DFS from the starting node
        # If shorter path exists, visit, if not, ignore
        # Count if all nodes are visited from the starting node
        # Return max if true, -1 if no
        dct = defaultdict(dict)
        for time in times:
            ui, vi, ti = time
            dct[ui][vi] = ti
        stack = []
        for node in dct[k]:
            stack.append((node, dct[k][node]))
        while stack:
            currentNode, currentDist = stack.pop()
            visitingNodes = dct[currentNode]
            for node in visitingNodes:
                if node == k: # Doesn't revisit node
                    continue
                if node not in dct[k]:
                    dct[k][node] = currentDist + dct[currentNode][node]
                    stack.append((node, currentDist + dct[currentNode][node]))
                else:
                    if dct[k][node] > currentDist + dct[currentNode][node]:
                        dct[k][node] = currentDist + dct[currentNode][node]
                        stack.append((node, currentDist + dct[currentNode][node]))
                    # Do nothing otherwise
        print(dct)
        visited = dct[k].keys()
        return -1 if len(visited) != n - 1 else max(dct[k].values())