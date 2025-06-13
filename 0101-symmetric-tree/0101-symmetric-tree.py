# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:  
        def helper(left, right):
            if not left and not right:
                return True

            if (left and not right) or (not left and right):
                return False

            if left.right and right.left:
                if left.right.val != right.left.val:
                    return False

            if left.left and right.right:
                if left.left.val != right.right.val:
                    return False

            return helper(left.right, right.left) and helper(left.left, right.right)
        
        if root.left and root.right:
            if root.left.val == root.right.val:
                return helper(root.left, root.right)
            else:
                return False
        else:
            if not root.left and not root.right:
                return True
            else:
                return False

        




            


        

        
            