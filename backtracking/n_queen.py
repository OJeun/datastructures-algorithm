def solveNQueens(n):
    res = []
    board = [['.'] * n for _ in range(n)]
    
    def convert_board(board):
        return ["".join(row) for row in board]
        
    def is_valid(row, column, board):
        for index in range(n):
            # Check row
            if "Q" == board[row][index]:
                return False
            # Check column
            if "Q" == board[index][column]:
                return False
        
        # Top left diagnose
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if "Q" == board[i][j]:
                return False
        
        # Down left diagnose
        for i, j in zip(range(row, n), range(column, -1, -1)):
            if "Q" == board[i][j]:
                return False
                
        # Top right diagnose
        for i, j in zip(range(row, -1, -1), range(column, n)):
            if "Q" == board[i][j]:
                return False
        
        # Down right diagnose
        for i, j in zip(range(row, n), range(column, n)):
            if "Q" == board[i][j]:
                return False
            
        return True
    
    def place_next_queen(row):
        if row == n:
            res.append(convert_board(board))
            return
            
        for column in range(n):
            if is_valid(row, column, board):
                board[row][column] = "Q"
                place_next_queen(row + 1)
                board[row][column] = "."
                
    place_next_queen(0)
    return res
                
print(solveNQueens(4))