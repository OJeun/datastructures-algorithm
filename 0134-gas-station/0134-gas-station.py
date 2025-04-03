class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_index = 0
        tank = 0
        total = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff

            if tank < 0:
                start_index = i + 1
                tank = 0

        return start_index if total >= 0 else -1