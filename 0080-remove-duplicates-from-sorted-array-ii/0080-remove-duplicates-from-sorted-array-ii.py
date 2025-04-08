class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = curr = 0

        while curr < len(nums):
            start_val = curr

            while curr < len(nums) - 1 and nums[curr] == nums[curr+1]:
                curr += 1

            duplicates = curr - start_val + 1
            steps = min(2, duplicates)

            for _ in range(steps):
                nums[start] = nums[curr]
                start += 1

            curr += 1

        return start
                
               
                

        


            