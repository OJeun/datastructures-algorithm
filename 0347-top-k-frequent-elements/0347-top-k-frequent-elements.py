class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} # key: num, value: frequnency
        output = []

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for _ in range(k):
            max_freq_value = 0
            max_freq = 0
            for value, freq in frequency.items():
                if freq > max_freq:
                    max_freq_value = value
                    max_freq = freq

            frequency.pop(max_freq_value)
                
            output.append(max_freq_value)

        return output
                

