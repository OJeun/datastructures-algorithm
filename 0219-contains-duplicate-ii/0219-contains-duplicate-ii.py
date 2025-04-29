class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_index = {}

        for i, num in enumerate(nums):
            index = num_index.get(num)

            if index is None:
                num_index[num] = i
            else:
                if abs(i - index) <= k:
                    return True
                else:
                    num_index[num] = i
        
        return False
            