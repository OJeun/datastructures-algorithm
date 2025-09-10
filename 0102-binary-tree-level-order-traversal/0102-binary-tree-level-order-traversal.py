# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([])
        output = []

        if not root:
            return output

        queue.append((root, 0))
        output.append([])

        while queue:
            node, level = queue.popleft()

            if len(output) < level + 1:
                output.append([])

            output[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return output
            