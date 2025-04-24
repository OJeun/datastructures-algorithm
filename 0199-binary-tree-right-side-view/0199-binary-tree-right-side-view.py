# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque([root])
        result = []

        while que:
            length = len(que)
            
            for i in range(length):
                node = que.popleft()
                if node:
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)

                    if i == (length - 1):
                        result.append(node.val)

        return result
                