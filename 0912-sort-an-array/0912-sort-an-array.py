class Solution:
    # merge helper funciton
    def merge(self, l1, l2) -> List[int]:
        output = []
        first, second = 0, 0
        while first < len(l1) and second < len(l2):
            if l1[first] > l2[second]:
                output.append(l2[second])
                second += 1
            else:
                output.append(l1[first])
                first += 1

        while first < len(l1):
                output.append(l1[first])
                first += 1

        while second < len(l2):
                output.append(l2[second])
                second += 1   

        return output

    def sortArray(self, nums: List[int]) -> List[int]: # return sorted array
        # Base case => if length of nums is one
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])

        right = self.sortArray(nums[mid:])

        return self.merge(left, right)
