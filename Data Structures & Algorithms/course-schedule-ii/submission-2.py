class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = {i: 0 for i in range(numCourses)}
        outdegrees = defaultdict(list)
        for courseA, courseB in prerequisites:
            indegrees[courseA] += 1
            outdegrees[courseB].append(courseA)
        res = []
        current = [course for course in indegrees.keys() if indegrees[course] == 0]
        while current:
            res.extend(current)
            newCurrent = []
            # Delete learnt courses
            # Find next courses
            for course in current:
                nextCourses = outdegrees[course]
                for nextCourse in nextCourses:
                    indegrees[nextCourse] -= 1
                    if indegrees[nextCourse] == 0:
                        newCurrent.append(nextCourse)
            current = newCurrent
        return res if len(res) == numCourses else []