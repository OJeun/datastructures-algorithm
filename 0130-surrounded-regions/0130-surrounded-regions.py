class Solution:
    def solve(self, board: list[list[str]]) -> None:
        columns = len(board[0])
        rows = len(board)
        self.board = board
        self.seen = set()

        def dfs(r, c):
            self.seen.add((r,c))
            self.board[r][c] = "S"

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                calc_r, calc_c = r + dr, c + dc
                if calc_r >= 0 and calc_r < rows and calc_c >= 0 and calc_c < columns:
                    if self.board[calc_r][calc_c] == "O" and (calc_r, calc_c) not in self.seen:
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
                    if self.board[row][column] == "O" and (row, column) not in self.seen:
                        dfs(row, column)

                if row == 0 or row == rows - 1:
                     if self.board[row][column] == "O" and (row, column) not in self.seen:
                        dfs(row, column)

            
        updateBoard()