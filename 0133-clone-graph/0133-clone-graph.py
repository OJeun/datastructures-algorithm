class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        original_to_cloned = {}

        def dfs(current):
            if current in original_to_cloned:
                return original_to_cloned[current]

           
            copy = Node(current.val)
            original_to_cloned[current] = copy

            
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
