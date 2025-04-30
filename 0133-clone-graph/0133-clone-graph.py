"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        self.copy_dict = dict()

        def dfs(node):
            if node not in self.copy_dict:
                self.copy_dict[node] = Node(node.val)
            else:
                return self.copy_dict[node]

            for neighbor in node.neighbors:
                if neighbor not in self.copy_dict:
                    self.copy_dict[neighbor] = Node(neighbor.val)
                    dfs(neighbor)

                self.copy_dict[node].neighbors.append(self.copy_dict[neighbor])

        dfs(node)
        return self.copy_dict[node]
                