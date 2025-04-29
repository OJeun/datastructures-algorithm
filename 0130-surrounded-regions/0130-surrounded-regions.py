class Solution:
    def solve(self, board: List[List[str]]) -> None:
        columns = len(board[0])
        rows = len(board)
        self.board = board

        def dfs(r, c, track) -> bool:
            if (r <= 0 or c <= 0 or r >= rows - 1 or c >= columns - 1):
                return False if self.board[r][c] == "O" else True

            if (r, c) in track:
                return True

            if board[r][c] != "O":
                return True
                
            track.add((r, c))
            
            up = dfs(r-1, c, track)
            down = dfs(r+1, c, track)
            right = dfs(r, c+1, track)
            left = dfs(r, c-1, track)

            return up and down and right and left

        def updateBoard(track):
            print(track)
            for r, c in track:
                self.board[r][c] = "X"

        for row in range(rows):
            for column in range(columns):
                track = set()
                if board[row][column] == "O":
                    if dfs(row, column, track):
                        updateBoard(track)
