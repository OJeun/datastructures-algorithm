from collections import deque
class Solution:
    def shortestBridge(self, grid) -> int:
        size = len(grid)
        edges = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c): # this will find a first island
            grid[r][c] = "f"
            is_edge = False

            for offset_r, offset_c in directions:
                new_r = r + offset_r
                new_c = c + offset_c

                if 0 <= new_r < size and 0 <= new_c < size:
                    if grid[new_r][new_c] == 1:
                        dfs(new_r, new_c) 
                    elif grid[new_r][new_c] != "f":
                        is_edge = True
                else:
                    is_edge = True
                
            if is_edge:
                edges.append((r,c))

        def findFirstIsland(grid):
            for r in range(size):
                for l in range(size):
                    if grid[r][l] == 1:
                        dfs(r, l)
                        return
                    
        def bfs(edges):
            queue = deque(edges)
            min_bridge = 0

            while queue:
                n = len(queue)
                
                for _ in range(n):
                    r, c = queue.popleft()
                    for offsetR, offsetC in directions:
                        moved_r = r + offsetR
                        moved_c = c + offsetC   
                        if 0 <= moved_r < size and 0 <= moved_c < size:
                            if grid[moved_r][moved_c] == 1:
                                return min_bridge
                            elif grid[moved_r][moved_c] == 0:
                                grid[moved_r][moved_c] = "v"
                                queue.append((moved_r, moved_c))
                        
                min_bridge += 1

        findFirstIsland(grid)
        return bfs(edges)