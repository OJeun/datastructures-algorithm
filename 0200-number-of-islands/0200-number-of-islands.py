from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # define a variable to count the num of islands
        islands = 0
        # define two variables length of rows and columns 
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()

        # for loop to iterate a grid row
        for row in range(rows):
            # iterate columns of a row
            for column in range(columns):
                curr_cell = grid[row][column] 
                # if (row, column) is not visited
                if curr_cell == '1':
                    queue.append((row, column))
                    
                    # traverse the grid using bfs 
                    while len(queue) > 0:
                        r, c = queue.pop()
                        grid[r][c] = 'v'
                        # up, (r-1, c)
                        if r - 1 >= 0 and grid[r-1][c] == "1":
                            queue.append((r-1, c))

                        # down (r+1, c)
                        if r + 1 < rows and grid[r+1][c] == "1":
                            queue.append((r+1, c))

                        # left (r, c - 1)
                        if c - 1 >= 0 and grid[r][c - 1] == "1"  :
                            queue.append((r, c - 1))

                        # right (r, c + 1)
                        if c + 1 < columns and grid[r][c + 1] == "1":
                            queue.append((r, c + 1))
                    
                    islands += 1

        return islands
                        
                    