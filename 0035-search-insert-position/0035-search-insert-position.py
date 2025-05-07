class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(start, end):

            mid = (start + end) // 2

            if target == nums[mid]:
                return mid

            if start == end:
                return start + 1

            if target > nums[mid]:
                return binarySearch(mid+1, end)
            else:
                return binarySearch(start, mid - 1)

        return binarySearch(0, len(nums)-1)

