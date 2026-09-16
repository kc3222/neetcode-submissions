class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stack
        stack = []
        for i in range(len(asteroids)):
            aster = asteroids[i]
            explode = False
            while stack and stack[-1] > 0 and aster < 0:
                if abs(aster) > stack[-1]:
                    stack.pop()
                elif abs(aster) == stack[-1]:
                    stack.pop()
                    aster = 0
                else:
                    aster = 0
            if aster != 0:
                stack.append(aster)
        return stack