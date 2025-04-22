# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root) -> int:
        return self.helper(root, 0)
    

    def helper(self, node, num):
        if not node:
            return 0

        if not node.left and not node.right:
            num = 10 * num + node.val
            return num

        num = 10 * num + node.val

        left = self.helper(node.left, num)
        right = self.helper(node.right, num)
      
        return left + right
