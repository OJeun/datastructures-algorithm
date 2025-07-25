class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recursive(left, right):
            first_sub_tree, second_sub_tree = True, True

            if (not left.left and right.right) or (not left.right and right.left):
                return False

            if (left.left and not right.right) or (left.right and not right.left):
                return False

            if left.left and right.right:
                if left.left.val != right.right.val:
                    return False
                else:
                    first_sub_tree = recursive(left.left, right.right)
            
            if left.right and right.left:
                if left.right.val != right.left.val:
                    return False
                else:
                    second_sub_tree = recursive(right.left, left.right) 

            return first_sub_tree and second_sub_tree

        if not root.left and not root.right:
            return True

        if root.left and root.right and root.left.val == root.right.val:
            return recursive(root.left, root.right)
        
        return False