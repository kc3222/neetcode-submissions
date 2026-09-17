class Solution:
    def decodeString(self, s: str) -> str:
        char = []   # stack: decoded string built up before each '['
        nums = []   # stack: repeat count parsed before each '['
        cur = ""    # decoded string being built at current nesting level
        num = 0     # number currently being parsed (handles multi-digit)

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)          # accumulate multi-digit numbers
            elif ch == "[":
                char.append(cur)                  # save what we've built so far
                nums.append(num)                  # save the count for this level
                cur = ""                           # start fresh inside the brackets
                num = 0
            elif ch == "]":
                cur = char.pop() + cur * nums.pop()  # repeat and reattach to parent
            else:
                cur += ch                          # regular letter

        return cur