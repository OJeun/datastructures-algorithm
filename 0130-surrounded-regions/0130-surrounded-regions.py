class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])
        visited = [[0] * columns for _ in range(rows)]

        def dfs(r, c):
            if visited[r][c] == 'v':
                return

            visited[r][c] = 'v'
            board[r][c] = 'T'

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                moved_r = r + dr
                moved_c = c + dc
                if 0 <= moved_r < rows and 0 <= moved_c < columns:
                    if board[moved_r][moved_c] == 'O':
                        dfs(r + dr, c + dc)

        for row in [0, rows -1]:
            for column in range(columns):
                if board[row][column] == 'O':
                    dfs(row, column)

        # traver left and right edge columns
        for column in [0, columns - 1]:
            for row in range(rows):
                if board[row][column] == 'O':
                    dfs(row, column)

        
        for r in range(rows):
            for c in range(columns):
                cell = board[r][c]
                if cell == 'T':
                    board[r][c] = 'O'
                if cell == 'O':
                    board[r][c] = 'X'
            

        # nested for loop 
            # update T to 0
            # update 0 to X