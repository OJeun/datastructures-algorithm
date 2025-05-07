class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = 0 
        end = len(nums) - 1

        def findFirst(start, end):
            first = -1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    first = mid
                    end = mid - 1

                elif nums[mid] < target:
                    start = mid + 1
                
                elif nums[mid] > target:
                    end = mid - 1

            return first

        def findLast(start, end):
            last = -1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    last = mid
                    start = mid + 1

                elif nums[mid] < target:
                    start = mid + 1
                
                elif nums[mid] > target:
                    end = mid - 1

            return last

        first = findFirst(start, end)
        last = findLast(start, end)
        return [first, last]
                 


