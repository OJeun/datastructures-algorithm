class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # helper(start, end) -> int:
        def helper(start, end) -> int:
            # if start > end: return - 1 # target is not in nums
            if start > end:
                return -1
            # mid index in nums
            mid_index = (start + end) // 2
            mid = nums[mid_index]
            # compare mid with target
            # if tartget = mid: return the index of the target
            if mid == target:
                return mid_index

            # if target > mid: return helper(mid + 1, end)
            if target > mid:
                return helper(mid_index + 1, end)

            # else: return helper(start, mid - 1) 
            else:
                return helper(start, mid_index - 1)


        # return helper(0, len(nums) - 1)
        return helper(0, len(nums) - 1)