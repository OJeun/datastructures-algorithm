# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        self.count = 0

        while que:
            node = que.popleft()
            if node:
                self.count += 1
                
                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

        return self.count



