class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def recursive(index, candidate, total):
            if total == target:
                result.append(candidate[:])
                return

            if total > target:
                return
        

            for i in range(index, len(candidates)):
                number = candidates[i]
                candidate.append(number)
                recursive(i, candidate, total + number)
                candidate.pop()
                
        recursive(0, [], 0)
        return result