class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        output = []
        stack = []
        next_greater = dict()

        for num in nums2:
            curr = num
            while stack and curr > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = curr
                    
            stack.append(num)

        for num in nums1:
            if num in next_greater:
                output.append(next_greater[num])
            else:
                output.append(-1)

        return output
