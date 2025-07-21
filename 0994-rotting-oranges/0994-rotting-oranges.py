from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # elaps = 0 // to count the elaps
        rows = len(grid)
        columns = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque([])
        max_time = 0
        fresh_oranges = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                if grid[r][c] == 1:
                    fresh_oranges += 1

        while queue:
            r, l, elaps = queue.popleft()
            max_time = max(max_time, elaps)

            for dr, dl in directions:
                new_r = r + dr
                new_l = l + dl

                if 0 <= new_r < rows and 0 <= new_l < columns and grid[new_r][new_l] == 1:
                    grid[new_r][new_l] = 2
                    fresh_oranges -= 1
                    queue.append((new_r, new_l, elaps + 1))

        if fresh_oranges > 0:
            return -1
        else:
            return max_time
                    
