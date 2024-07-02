board = [
["5", "3", ".", ".", "7", ".", ".", ".", "."],
["6", ".", ".", "1", "9", "5", ".", ".", "."],
[".", "9", "8", ".", ".", ".", ".", "6", "."],
["8", ".", ".", ".", "6", ".", ".", ".", "3"],
["4", ".", ".", "8", ".", "3", ".", ".", "1"],
["7", ".", ".", ".", "2", ".", ".", ".", "6"],
[".", "6", ".", ".", ".", ".", "2", "8", "."],
[".", ".", ".", "4", "1", "9", ".", ".", "5"],
[".", ".", ".", ".", "8", ".", ".", "7", "9"]]

def condition_checker(i, j, num, board):
        # Check row
        if num in board[i]:
            return True
        # Check column
        for row in range(9):
            if num == board[row][j]:
                return True
        # Check grid
        grid_row = i // 3
        grid_column = j // 3
        for row in range(grid_row * 3, grid_row * 3 + 3):
            for column in range(grid_column * 3, grid_column * 3 + 3):
                if num == board[row][column]:
                    return True
        return False
                    
print(condition_checker(7, 2, "6", board))


