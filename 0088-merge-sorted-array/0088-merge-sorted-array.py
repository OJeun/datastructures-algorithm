class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        j = n - 1

        pointer = m - 1

        if j < 0:
            return

        while pointer > -1 and j > -1:
            if nums1[pointer] < nums2[j]:
                nums1[i] = nums2[j]
                j -= 1
                i -= 1
            else:
                nums1[i] = nums1[pointer] 
                pointer -= 1
                i -= 1

        while j >= 0:
            nums1[i] = nums2[j]
            i -= 1
            j -= 1