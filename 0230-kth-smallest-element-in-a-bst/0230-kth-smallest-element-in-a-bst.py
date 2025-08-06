# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def dfs(node):
            left, right = -1, -1

            if node and node.left:
                left = dfs(node.left)

            self.count += 1

            if self.count == k:
                return node.val

            if node and node.right:
                right = dfs(node.right) 

            return left if left != -1 else right

        return dfs(root)


