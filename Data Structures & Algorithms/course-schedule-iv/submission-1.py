class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build a query graph
        # For each query, do a BFS from u to see if it can reach v
        graph = defaultdict(list)
        for ai, bi in prerequisites:
            graph[bi].append(ai)
        
        # BFS
        res = []
        for uj, vj in queries:
            req = False
            stack = [vj]
            seen = {vj}  # global visited set, persists across all levels
            while stack:
                newStack = []
                for course in stack:
                    if course == uj:
                        req = True
                        break
                    for prq in graph[course]:
                        if prq not in seen:  # mark visited at push-time
                            seen.add(prq)
                            newStack.append(prq)
                if req:
                    break
                stack = newStack
            res.append(req)
        return res