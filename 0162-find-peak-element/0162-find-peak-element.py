class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binarySearch(start, end):
            mid = (start + end) // 2
            
            if start >= end:
                return start

            if nums[mid] < nums[mid+1]:
                return binarySearch(mid + 1, end)
            else:
                return binarySearch(start, mid)

        return binarySearch(0, len(nums) - 1)