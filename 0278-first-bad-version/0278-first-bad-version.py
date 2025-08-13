# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        def binarySearch(start, end):
            mid = (start + end) // 2

            if isBadVersion(mid) == True:
                if mid == start or isBadVersion(mid-1) == False:
                    return mid
                
                else:
                    return binarySearch(start, mid - 1)

            else: # isBadVersion(mid) == False
                return binarySearch(mid + 1, end)
                
        return binarySearch(0, n)
