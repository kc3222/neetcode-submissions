class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 0:
            visited.add(n)
            if n == 1:
                return True
            else:
                new_n = 0
                for i in range(len(str(n))):
                    new_n += int(str(n)[i]) ** 2
                if new_n in visited:
                    return False
                n = new_n
        return True