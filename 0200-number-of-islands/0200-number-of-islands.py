from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        self.count = 0
        self.rows = len(grid)
        self.columns = len(grid[0])

        def bfs(r, c, grid):
            queue = deque([(r, c)])
            grid[r][c] = "x"
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                r, c = queue.popleft()
                for offset_r, offset_c in directions:
                    new_r = r + offset_r
                    new_c = c + offset_c

                    if 0 <= new_r < self.rows and 0 <= new_c < self.columns:
                        if grid[new_r][new_c] == "1":
                            queue.append((new_r, new_c))
                            grid[new_r][new_c] = "x"

            self.count += 1
        
        # traverse the grid 
        for r in range(self.rows):
            for c in range(self.columns):
                if grid[r][c] == "1":
                    bfs(r, c, grid)

        return self.count

