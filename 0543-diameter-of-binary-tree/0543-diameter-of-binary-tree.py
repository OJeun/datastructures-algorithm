# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def recursion(node): # return max diameter from the input node
            if node is None:
                return 0

            left, right = 0, 0

            if node.left:
                left = recursion(node.left) + 1 
            
            if node.right:
                right = recursion(node.right) + 1

            self.diameter = max(self.diameter, right + left)

            return max(left, right)

        recursion(root)
        return self.diameter 
