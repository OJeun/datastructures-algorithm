# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left >= pre_right or in_left >= in_right:
                return None


            inorder_root = 0 
            for i in range(in_right - in_left + 1):
                if inorder[in_left + i] == preorder[pre_left]:
                    inorder_root = in_left + i # 1
                    break

            left_size = inorder_root - in_left # 1 - 0 = 1

            left_subtree = helper(pre_left + 1, pre_left + 1 + left_size, in_left, in_left + left_size)
            right_subtree = helper(pre_left + 1 + left_size, pre_right, inorder_root + 1, in_right)

            root_value = preorder[pre_left]
            root_node = TreeNode(root_value)
            if left_subtree:
                root_node.left = left_subtree
            
            if right_subtree:
                root_node.right = right_subtree

            return root_node

        length = len(preorder)

        return helper(0, length, 0, length)




       



        
            