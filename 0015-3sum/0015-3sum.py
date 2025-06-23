class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_length = len(nums)
        output = []

        for curr in range(nums_length - 2):
            if nums[curr] > 0:
                return output
                
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue

            left = curr + 1
            right = nums_length - 1

            

            while left < right:
                three_sum = nums[curr] + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1

                elif three_sum < 0:
                    left += 1

                else:
                    output.append([nums[curr], nums[left], nums[right]])
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1
                    
        return output