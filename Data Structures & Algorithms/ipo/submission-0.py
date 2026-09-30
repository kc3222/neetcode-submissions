class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Sort both lists by capital
        # Use a heap to add profit, pop the top one
        # Calculate new capital, add new potential profit to the heap
        # Repeat
        capital, profits = map(list, zip(*sorted(zip(capital, profits))))
        heap = []
        currProjectIdx = 0
        
        for i in range(k):
            # Add all new profits to heap
            while currProjectIdx < len(capital) and capital[currProjectIdx] <= w:
                if profits[currProjectIdx] > 0: # Only do profitable project
                    heapq.heappush(heap, -profits[currProjectIdx])
                currProjectIdx += 1
            # Add the best profit to w
            if not heap: # No project to do
                return w
            profit = -heapq.heappop(heap)
            w += profit

        return w