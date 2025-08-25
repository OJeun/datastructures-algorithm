# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, currSum):
            if not node:
                return False

            if currSum == targetSum and not node.left and not node.right:
                return True

            left, right = False, False

            if node.left:
                left = dfs(node.left, currSum + node.left.val)

            if node.right:
                right = dfs(node.right, currSum + node.right.val)

            return left or right

        return dfs(root, root.val) if root else False