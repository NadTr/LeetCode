class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        tank = 0
        stop = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                stop = i + 1

        return stop if i < len(gas) else -1
