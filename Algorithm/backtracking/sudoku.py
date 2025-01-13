# Time Complexity = O(1)
# 9 ^ 81 = 9 ^ maximum empty cells
# Space Complexity = O(1)
# 9 * 9 = n * n

def solveSudoku(board):
    SUDOKU_SIZE = 9

    def helper():
        for row in range(SUDOKU_SIZE):
            for column in range(SUDOKU_SIZE):
                if board[row][column] == ".":
                    for num in '123456789':
                        if is_valid(row, column, num):
                            board[row][column] = num
                            if helper(): return True
                            board[row][column] = "."
                    return False
        return True
                    
                
    def is_valid(row, column, num):
        for index in range(SUDOKU_SIZE):
            # Column check
            if num == board[index][column]:
                return False
            
            # Row check
            if num == board[row][index]:
                return False
            
            # Grid check
            curr_row = (row // 3) * 3 + index // 3
            curr_col = (column // 3) * 3 + index % 3
            if num == board[curr_row][curr_col]:
                return False
                
            return True
    helper()
    
