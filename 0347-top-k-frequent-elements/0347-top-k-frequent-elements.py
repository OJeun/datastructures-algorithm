import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        # Define dictionary looping through nums => key: nums, value: frequency
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        # Define a min heap using heapq initializing it with empty list
        min_heap = []


        # Iterate through dictionary
        for key, freq in frequencies.items():
            heapq.heappush(min_heap, (freq, key))
            # if the heap size > k:
                # pop the entry with minimum frequency
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            

        for index in range(len(min_heap)):
            min_heap[index] = min_heap[index][1]

        return min_heap