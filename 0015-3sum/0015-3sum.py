class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            first = i + 1
            second = n - 1

            while first < second:
                three_sum =  nums[i] + nums[first] + nums[second]
                if three_sum > 0:
                    second -= 1
                elif three_sum < 0:
                    first += 1
                else: 
                    res.append([nums[i], nums[first], nums[second]])
                    first += 1
                    second -= 1

                    while first < second and nums[first] == nums[first - 1]:
                        first += 1

                    while first < second and nums[second] == nums[second + 1]:
                        second -= 1    
        return res