# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val_to_index = {val:index for index, val in enumerate(inorder)}
    
        def helper(post_left, post_right, in_left, in_right):
            if post_left >= post_right or in_left >= in_right:
                return None

            root_index = val_to_index[postorder[post_right - 1]] # 1
            left_subtree_size = root_index - in_left # 1 - 0 = 1
            


            left_subtree_root = helper(post_left, post_left + left_subtree_size, in_left, in_left + left_subtree_size)
            right_subtree_root = helper(post_left + left_subtree_size, post_right - 1, root_index + 1, in_right)
            
            node = TreeNode(postorder[post_right - 1])
            if left_subtree_root:
                node.left = left_subtree_root
            
            if right_subtree_root:
                node.right = right_subtree_root

            return node

        length = len(postorder)
        return helper(0, length, 0, length)


    
    