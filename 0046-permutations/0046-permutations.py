class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []
        permutation = []
        track = set()

        def backtracking():
            if len(permutation) == 3:
                output.append(permutation[:])
                return
            
            for index in range(len(nums)):
                curr_num = nums[index]
                if curr_num not in track:
                    permutation.append(curr_num)
                    track.add(curr_num)
                    backtracking()
                    permutation.pop()
                    track.remove(curr_num)

        backtracking()
        return output