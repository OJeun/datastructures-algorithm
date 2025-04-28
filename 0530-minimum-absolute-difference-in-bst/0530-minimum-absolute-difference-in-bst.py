# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float('inf')
        self.sorted_list = []

        def sort_binary_tree(node):
            if not node:
                return None
            
            left = sort_binary_tree(node.left)
            self.sorted_list.append(node.val)
            right = sort_binary_tree(node.right)

        def find_minimum_diff(sorted_list):
            for i in range(len(sorted_list) -1):
                diff = abs(sorted_list[i] - sorted_list[i+1])
                self.min = min(diff, self.min)

        sort_binary_tree(root)
        find_minimum_diff(self.sorted_list)

        return self.min