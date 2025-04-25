# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_sum = 0
        que = deque([root])
        level_ave = []

        while que:
            length = len(que)
            level_sum = 0
            for i in range(length):
                node = que.popleft()
                level_sum += node.val
                if node and node.left:
                    que.append(node.left)
                if node and node.right:
                    que.append(node.right)
                if i == length - 1:
                    level_ave.append(level_sum / length)
        return level_ave

