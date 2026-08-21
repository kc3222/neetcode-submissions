import bisect

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for t in temperatures]
        stack = [(temperatures[-1], len(temperatures) - 1)]
        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return res