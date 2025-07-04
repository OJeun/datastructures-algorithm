# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # handle edge case when root is None => 0
        if not root: 
            return 0

        # DFS recursively => helper func(node) -> return the depth from that node to leave
        def dfs(node) -> int:
            if node is None:
                return 0
           
            # left side subtree's depth
            left = dfs(node.left)
            # right side subtree's depth
            right = dfs(node.right)

            # return max(left, right)
            return max(left, right) + 1 

        # return helper with root 
        return dfs(root)