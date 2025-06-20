# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 1   
        height = 1
        stack = [(root, 1)]

        while stack:
            curr, height = stack.pop()
            left = curr.left
            right = curr.right

            if left:
                stack.append((left, height + 1))
                
            if right:
                stack.append((right, height + 1))
                

            max_depth = max(max_depth, height)
            

        return max_depth