# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return 0

            if not node.left and not node.right:
                return depth

            if node.left and node.right:
                return min(
                    dfs(node.left, depth + 1),
                    dfs(node.right, depth + 1)
                )
            elif not node.left:
                return dfs(node.right, depth + 1)
            else:
                return dfs(node.left, depth + 1)

        return dfs(root, 1)
