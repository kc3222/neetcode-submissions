class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers
        i, j = 0, len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i + 1, j + 1]