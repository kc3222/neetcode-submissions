class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = 0
        for i in range(len(gas)):
            if gas[i] > cost[i]:
                currGas = gas[i] - cost[i]
                finish = True
                for j in range(len(gas) - 1):
                    nxStop = (i + j + 1 + len(gas)) % len(gas)
                    if currGas + gas[nxStop] - cost[nxStop] < 0:
                        finish = False
                        break
                    else:
                        currGas = currGas + gas[nxStop] - cost[nxStop]
                if finish:
                    res = i
        return res
