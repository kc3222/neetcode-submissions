class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_a = heapq.heappop(stones)
            stone_b = heapq.heappop(stones)
            new_stone = abs(stone_a) - abs(stone_b)
            heapq.heappush(stones, -new_stone)
        return abs(stones[0])