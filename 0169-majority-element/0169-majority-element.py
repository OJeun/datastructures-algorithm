class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        max_item = nums[0]

        for index in range(1, len(nums)):
            curr = nums[index]
            prev = nums[index-1]

            if count == 0:
                max_item = curr

            if curr == max_item:
                count += 1
            else:
                count -= 1
                         
        return max_item
         