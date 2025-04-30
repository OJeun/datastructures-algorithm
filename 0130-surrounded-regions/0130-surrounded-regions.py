class Solution:
    def solve(self, board: list[list[str]]) -> None:
        columns = len(board[0])
        rows = len(board)
        self.board = board

        def dfs(r, c):
            self.board[r][c] = "S"

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                calc_r, calc_c = r + dr, c + dc
                if 0 <= calc_r < rows and 0 <= calc_c < columns and board[calc_r][calc_c] == "O":
                    dfs(calc_r, calc_c)

        def updateBoard():
            for row in range(rows):
                for column in range(columns):
                    if self.board[row][column] == "O":
                        self.board[row][column] = "X"
                    if self.board[row][column] == "S":
                        self.board[row][column] = "O"

        for row in range(rows):
            for column in range(columns):
                if (0 < row < rows - 1) and (column == 0 or column == columns - 1):
                    if self.board[row][column] == "O":
                        dfs(row, column)

                if row == 0 or row == rows - 1:
                     if self.board[row][column] == "O":
                        dfs(row, column)

            
        updateBoard()