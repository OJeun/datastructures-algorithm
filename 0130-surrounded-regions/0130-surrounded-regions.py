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

        for column in range(columns):
            if board[rows - 1][column] == 'O':
                dfs(rows - 1, column)
            if board[0][column] == 'O':
                dfs(0, column)

        # traver left and right edge columns
        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][columns - 1] == 'O':
                dfs(row, columns - 1)

        
        for r in range(rows):
            for c in range(columns):
                cell = board[r][c]
                if cell == 'T':
                    board[r][c] = 'O'
                if cell == 'O':
                    board[r][c] = 'X'
