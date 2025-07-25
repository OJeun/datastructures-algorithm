class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recursive(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (left.val == right.val
            and recursive(left.left, right.right)
            and recursive(right.left, left.right)
            )

        return recursive(root.left, root.right)