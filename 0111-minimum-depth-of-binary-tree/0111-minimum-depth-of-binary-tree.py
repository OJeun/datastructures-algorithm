# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = float('inf')

        def dfs(node, depth):
            if not node.left and not node.right:
                return depth
            
            left, right = float('inf'), float('inf')

            if node.left:
                left = dfs(node.left, depth + 1)
            if node.right:
                right = dfs(node.right, depth + 1)

            return min(left, right)
        
        if not root:
            return 0
        else:
            return dfs(root, 1)