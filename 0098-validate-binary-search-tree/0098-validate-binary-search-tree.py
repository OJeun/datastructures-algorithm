# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # define recursive helper funtion(node, boundary)
        def helper(node, max_val, min_val):
            if node is None:
                return True

            if not(min_val < node.val < max_val):
                return False

            left_is_valid = helper(node.left, node.val, min_val)

            right_is_valid = helper(node.right, max_val, node.val)

            return left_is_valid and right_is_valid

            
            

        return helper(root, float('inf'), float('-inf'))
