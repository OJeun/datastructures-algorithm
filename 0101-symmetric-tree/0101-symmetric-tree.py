# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        que = deque([(root.left, root.right)])

        if not root:
            return True

        while que:
            p, q = que.popleft()

            if not p and not q:
                continue
            
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            que.append((p.left, q.right))
            que.append((p.right, q.left))

        return True