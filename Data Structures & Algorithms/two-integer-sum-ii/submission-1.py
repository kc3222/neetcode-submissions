class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Loop and binary search
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[-1] == target:
                return [i + 1, len(numbers)]
            elif numbers[i] + numbers[-1] < target:
                continue
            low = i + 1
            high = len(numbers) - 1
            middle = (low + high) // 2
            while low < middle:
                currSum = numbers[i] + numbers[middle]
                if currSum == target:
                    return [i + 1, middle + 1]
                elif currSum < target:
                    low = middle
                else:
                    high = middle
                middle = (low + high) // 2
            if numbers[i] + numbers[low] == target:
                return [i + 1, low + 1]
            if numbers[i] + numbers[high] == target:
                return [i + 1, high + 1]
        return [0, 1]