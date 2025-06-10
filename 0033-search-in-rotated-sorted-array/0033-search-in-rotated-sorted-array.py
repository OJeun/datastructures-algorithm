class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binarySearch(left, right):
            mid = (left + right) // 2
            mid_element = nums[mid]

            if mid_element == target:
                return mid

            if left >= right:
                return -1

            if nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    return binarySearch(left, mid -1)
                else:
                    return binarySearch(mid+1, right)
            else:
                if target > nums[mid] and target <= nums[right]:
                    return binarySearch(mid+1, right)
                else:
                    return binarySearch(left, mid -1)
        
        n = len(nums)
        return binarySearch(0, n-1)