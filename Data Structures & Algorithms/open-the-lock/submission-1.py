class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        # BFS
        def neighbors(state):
            res = []
            for i in range(4):                    # each of the 4 wheels
                d = int(state[i])
                for delta in (1, -1):              # turn it forward or backward one slot
                    nd = (d + delta) % 10          # wrap around 0-9
                    nextNum = state[:i] + str(nd) + state[i+1:]
                    if nextNum not in deadends:
                        res.append(nextNum)
                        deadends.add(nextNum)
            return res
        
        stack = ['0000']
        deadends.add('0000')
        count = 0
        while stack:
            nextStack = []
            for num in stack:
                if num == target:
                    return count
                nextStack.extend(neighbors(num))
            count += 1
            stack = nextStack
        return -1