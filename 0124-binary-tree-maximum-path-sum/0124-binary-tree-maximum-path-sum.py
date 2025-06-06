# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') 
        
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            three_sum = node.val + left + right

            self.max_sum = max(self.max_sum, three_sum, node.val, max(left, right) + node.val)

            return max(left, right) + node.val

        dfs(root)
        return self.max_sum


            

                


            
            