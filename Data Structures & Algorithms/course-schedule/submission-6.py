class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegrees = defaultdict(int)
        outDegrees = {n: [] for n in range(numCourses)}
        for prereq in prerequisites:
            inDegrees[prereq[0]] += 1
            outDegrees[prereq[1]].append(prereq[0])
        
        current = []
        for i in range(numCourses):
            if inDegrees[i] == 0:
                current.append(i)
        learnt = []
        while current:
            for course in current:
                learnt.append(course)
                del inDegrees[course]
                for outDegree in outDegrees[course]:
                    inDegrees[outDegree] -= 1 # Reduce prereq for learnt courses
            current = [key for key in inDegrees if inDegrees[key] == 0]

        return len(learnt) == numCourses