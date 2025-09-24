class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        rows = len(board)
        columns = len(board[0])
        seen = [["x" for _ in range(columns)] for _ in range(rows)]

        def bfs(r, c, index):

            if index >= len(word):
                return True
            
            for offset_r, offset_c in directions:
                row = r + offset_r
                column = c + offset_c

                if 0 <= row < rows and 0 <= column < columns:
                    if seen[row][column] =="x" and board[row][column] == word[index]:
                        seen[row][column] = "v"
                        if bfs(row, column, index + 1) == False:
                            seen[row][column] = "x"
                        else:
                            return True
                            
            return False
        
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == word[0]:
                    seen[r][c] = "v"
                    if bfs(r, c, 1):
                        return True
                    seen[r][c] = "x"
        
        return False