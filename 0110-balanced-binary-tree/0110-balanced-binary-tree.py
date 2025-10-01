class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) 
            right = dfs(node.right) 

            if abs(left - right) > 1:
                return -1

            if left == -1 or right == -1:
                return -1
            else:
                return max(left + 1, right + 1)

        
        if dfs(root) == -1:
            return False
        else:
            return True