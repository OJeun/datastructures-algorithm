class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []

        visited = set()
        def backtracking(permutation):
            for num in nums:
                if num not in visited:
                    permutation.append(num)
                    visited.add(num)
                    backtracking(permutation)
                    permutation.pop()
                    visited.remove(num)
                
            if len(permutation) == n:
                permutations.append(permutation[:])

            return
        backtracking([])
        return permutations