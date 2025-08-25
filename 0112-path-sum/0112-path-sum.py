# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            stack = [(root, root.val)] 
        else:
            return False

        while stack:
            node, currSum = stack.pop()

            if currSum == targetSum and not node.left and not node.left:
                return True
            
            if node.left:
                stack.append((node.left, currSum + node.left.val))

            if node.right:
                stack.append((node.right, currSum + node.right.val))

        return False

        
        # def dfs(node, currSum):
        #     if not node:
        #         return False

        #     if currSum == targetSum and not node.left and not node.right:
        #         return True

        #     left, right = False, False

        #     if node.left:
        #         left = dfs(node.left, currSum + node.left.val)

        #     if node.right:
        #         right = dfs(node.right, currSum + node.right.val)

        #     return left or right

        # return dfs(root, root.val) if root else False