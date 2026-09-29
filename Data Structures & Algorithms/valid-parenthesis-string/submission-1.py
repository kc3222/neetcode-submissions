class Solution:
    def checkValidString(self, s: str) -> bool:
        # Counter forward to handle )*
        openCounter = 0
        anyCounter = 0
        for i in range(len(s)):
            if s[i] == '(':
                openCounter += 1
            elif s[i] == ')':
                openCounter -= 1
                if openCounter < 0:
                    if anyCounter == 0:
                        return False
                    else:
                        anyCounter -= 1
                        openCounter += 1
            else:
                anyCounter += 1
        if openCounter != 0 and anyCounter < openCounter:
            return False
        # Counter backward to handle *(
        closeCounter = 0
        anyCounter = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                closeCounter -= 1
                if closeCounter < 0:
                    if anyCounter == 0:
                        return False
                    else:
                        anyCounter -= 1
                        closeCounter += 1
            elif s[i] == ')':
                closeCounter += 1
            else:
                anyCounter += 1
        if closeCounter != 0 and anyCounter < closeCounter:
            return False
        return True