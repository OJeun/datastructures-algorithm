# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def recursive(node, total):
            total += node.val

            if not node.left and not node.right:
                return total == targetSum

            left, right = False, False
            
            if node.left:
                left = recursive(node.left, total)

            if node.right:
                right = recursive(node.right, total)

            return left or right

        return recursive(root, 0)