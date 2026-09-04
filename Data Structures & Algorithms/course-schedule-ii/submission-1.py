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
            # Delete learnt courses
            # Find next courses
            for course in current:
                del indegrees[course]
                nextCourses = outdegrees[course]
                for nextCourse in nextCourses:
                    indegrees[nextCourse] -= 1
            current = [course for course in indegrees.keys() if indegrees[course] == 0]
        return res if len(res) == numCourses else []