import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        i = idx - 1
        j = idx
        res = []
        while 0 <= i and j <= len(arr) - 1 and len(res) < k:
            if abs(arr[i] - x) <= abs(arr[j] - x):
                res.append(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1
        if i < 0 and len(res) < k:
            res.extend(arr[j: j + k - len(res)])
        if j > len(arr) - 1 and len(res) < k:
            res.extend(arr[i + len(res) - k + 1: i + 1])
        return sorted(res)