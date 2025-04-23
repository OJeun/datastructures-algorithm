"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        que = deque([])
        que.append(root)

        if not root:
            return root

        while que:
            length = len(que)
            for i in range(length):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
                if i == length - 1:
                    node.next = None
                else:
                    node.next = que[0]

        return root