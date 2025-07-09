class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start = 0, end = length - 1
        start = 0
        end = len(numbers) - 1
        
        # while start <= end:
        while start <= end:
            # sum of start and end
            two_sum = numbers[start] + numbers[end]

            if two_sum < target:
                # increase start by 1
                start += 1

            # elif sum > target:
            elif two_sum > target:
                # decrease end by 1
                end -= 1

            else:
                return [start + 1, end + 1]

