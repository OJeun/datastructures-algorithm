class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small_poiner = 0
        large_pointer = len(numbers) - 1

        while small_poiner < large_pointer:
            if numbers[small_poiner] + numbers[large_pointer] == target:
                return [small_poiner + 1, large_pointer + 1]

            if numbers[small_poiner] + numbers[large_pointer] > target:
                large_pointer -= 1

            if numbers[small_poiner] + numbers[large_pointer] < target:
                small_poiner += 1



