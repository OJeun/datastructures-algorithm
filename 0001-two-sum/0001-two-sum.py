class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = dict()
        pair = []
        nums_length = len(nums)

        for index in range(nums_length):
            num = nums[index]
            rest = target - num
            if rest in track:
                pair.append(track[rest])
                pair.append(index)
                return pair
            else:
                track[num] = index

        return pair
            
