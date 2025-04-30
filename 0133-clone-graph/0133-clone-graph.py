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

        que = deque()
        que.append(node)

        original_to_cloned = dict()

        while que:
            vertex = que.popleft()

            if vertex not in original_to_cloned:
                new_node = Node(vertex.val)
                original_to_cloned[vertex] = new_node

            cloned_vertex = original_to_cloned[vertex]

            for neighbor in vertex.neighbors:
                copied_neighbor = original_to_cloned.get(neighbor)
                if copied_neighbor is None:
                    new_neighbor = Node(neighbor.val)
                    original_to_cloned[neighbor] = new_neighbor
                    que.append(neighbor)
                
                original_to_cloned[neighbor].neighbors.append(cloned_vertex)

                

        return original_to_cloned[node]
