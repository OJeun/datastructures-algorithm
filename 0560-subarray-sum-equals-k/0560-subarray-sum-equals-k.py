from collections import defaultdict
class Solution:
    # nums = [1, 2, 3, -2, 5], k = 3
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum_dict = defaultdict(int)
        acc = 0
        count = 0

        for num in nums:
            acc += num

            if acc == k:
                count += 1
            
            if acc - k in sum_dict:
                count += sum_dict[acc - k]

            sum_dict[acc] += 1

        return count