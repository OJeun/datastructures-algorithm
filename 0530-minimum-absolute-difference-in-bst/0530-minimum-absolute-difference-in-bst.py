# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float('inf')
        self.prev = None

        def sort_binary_tree(node):
            if not node:
                return None
            
            sort_binary_tree(node.left)
            
            if self.prev:
                self.min = min(self.min, abs(self.prev.val - node.val))
            self.prev = node

            sort_binary_tree(node.right)


        sort_binary_tree(root)
        return self.min