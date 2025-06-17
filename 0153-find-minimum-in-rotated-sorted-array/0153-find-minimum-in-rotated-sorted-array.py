class Solution:
    def findMin(self, nums: list[int]) -> int:
        minimum = nums[0]

        n = len(nums)
        
        def binarySearch(start, end, minimum):
            if start >= end:
                return minimum

            mid = (start + end) // 2
            mid_element = nums[mid]

            # Check if the mid element is minimum
            minimum = min(minimum, mid_element)

            # Either right or left side of mid is sorted, Or both
            # Both side are sorted
            if nums[mid+1] <= nums[end] and nums[start] <= nums[mid-1]:
                minimum = min(nums[mid+1], nums[start], minimum)
                return minimum
            
            # Check right side is sorted
            if nums[mid+1] <= nums[end]:
                minimum = min(minimum, nums[mid+1])
                return binarySearch(start, mid - 1, minimum)
            
            # Check left side is sorted
            if nums[start] <= nums[mid-1]:
                minimum = min(minimum, nums[start])
                return binarySearch(mid+1, end, minimum)

        return binarySearch(0, n-1, minimum)