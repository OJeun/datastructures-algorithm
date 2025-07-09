class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums in-place
        nums.sort()
        # triplets = [] => include all the triplets whose sum add up to 0
        triplets = []


        # while first is in boundary(first < length of nums)
        for first, value in enumerate(nums):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            
            second = first + 1
            third = len(nums) - 1

            while second < third:
                complement = -nums[first]
                two_sum = nums[second] + nums[third]
                if two_sum < complement: 
                    # move second pointer to the next 
                    second += 1

                elif two_sum > complement:
                    # decrease third by 1
                    third -= 1

                # else ==> find 0!
                else:
                    triplets.append([nums[first], nums[second], nums[third]])
                    third -= 1
                    second += 1
                    while second < third and nums[second] == nums[second -1]:
                        second += 1
                    


        # return triplets
        return triplets

                



