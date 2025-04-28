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

        def in_order(node):
            if not node:
                return

            in_order(node.left)

            if self.prev is not None:
                self.min = min(self.min, node.val - self.prev)
            self.prev = node.val

            in_order(node.right)

        in_order(root)
        return self.min
