from heapq import heapify,heappush,heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        min_sum = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(min_sum, (nums1[i] + nums2[0], i, 0))

        while len(result) < k:
            two_sum, i, j = heapq.heappop(min_sum)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(min_sum, (nums1[i] + nums2[j+1], i, j+1))

        return result

        
                


            



            