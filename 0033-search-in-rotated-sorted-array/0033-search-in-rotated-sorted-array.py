class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def recursion(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]: # first half is ascending
                    return recursion(start, mid - 1)
                else:
                    return recursion(mid+1, end)
            else:
                if nums[mid] < target <= nums[end]:
                    return recursion(mid+1, end)
                else:
                    return recursion(start, mid - 1)

        
        return recursion(0, len(nums) - 1)
