class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        res_distance = []
        for point in points:
            distance = (abs(point[0]) ** 2 + abs(point[1]) ** 2)**0.5
            res.append(point)
            res_distance.append(distance)
        res_distance, res = zip(*sorted(zip(res_distance, res)))
        return list(res)[:k]