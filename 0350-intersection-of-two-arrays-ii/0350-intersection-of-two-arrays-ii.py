class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = dict()
        intersection = []

        for num in nums1:
            nums1_dict[num] = nums1_dict.get(num, 0) + 1

        for num in nums2:
            is_num_in_nums1 = nums1_dict.get(num)
            if is_num_in_nums1 and is_num_in_nums1 > 0:
                nums1_dict[num] -= 1
                intersection.append(num)

        return intersection