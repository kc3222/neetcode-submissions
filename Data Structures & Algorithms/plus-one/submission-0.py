class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        digits = digits[::-1]
        for i in range(len(digits)):
            prevDigit = digits[i]
            digits[i] = (prevDigit + rem) % 10
            rem = (prevDigit + rem) // 10
        if rem:
            digits.append(1)
        return digits[::-1]