class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        acc = 0
        result = 0
        frequency = dict()
        frequency[0] = 1

        for num in nums:
            acc += num

            if -(k - acc) in frequency:
                result += frequency[-(k - acc)]

            frequency[acc] = frequency.get(acc,0) + 1

        return result