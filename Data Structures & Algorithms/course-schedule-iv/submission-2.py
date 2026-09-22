from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for ai, bi in prerequisites:
            graph[bi].append(ai)

        res = []
        for uj, vj in queries:
            req = False
            stack = deque([vj])
            seen = {vj}
            while stack:
                course = stack.popleft()
                for prq in graph[course]:
                    if prq in seen:
                        continue
                    if prq == uj:      # check at discovery
                        req = True
                        break
                    seen.add(prq)
                    stack.append(prq)
                if req:
                    break
            res.append(req)
        return res