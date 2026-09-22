class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build a query graph
        # For each query, do a BFS from u to see if it can reach v
        graph = defaultdict(list)
        for prereq in prerequisites:
            ai, bi = prereq
            graph[bi].append(ai)
        
        # BFS
        res = []
        for query in queries:
            uj, vj = query
            req = False
            stack = [vj]
            while stack:
                newStack = []
                for course in stack:
                    if course == uj:
                        req = True
                        break
                    newStack.extend(graph[course])
                if req:
                    stack = []
                else:
                    stack = list(set(newStack))
            if req:
                res.append(True)
            else:
                res.append(False)
        return res