class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = dict()
        output = []

        for num in nums2:
            seen[num] = seen.get(num, 0) + 1


        for num in nums1:
            frequency = seen.get(num)
            if frequency and frequency > 0:
                output.append(num)
                seen[num] -= 1

        return output

