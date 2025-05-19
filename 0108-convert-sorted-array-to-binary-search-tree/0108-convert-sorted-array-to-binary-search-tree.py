# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start, end):
            if start > end:
                return None

            mid = (start + end) // 2

            sub_root_value = nums[mid]
            sub_root = TreeNode(sub_root_value)

            sub_left = helper(start, mid - 1)
            sub_right = helper(mid + 1, end)

            sub_root.left = sub_left
            sub_root.right = sub_right

            return sub_root

        return helper(0, len(nums) - 1)
