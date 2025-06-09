class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        rows = len(board)
        columns = len(board[0])

        def helper(row, column, char_index):
            if char_index == len(word):
                return True

            if row == rows or column == columns or row < 0 or column < 0:
                return False

            targeted_char = word[char_index]
            current_char = board[row][column]
            
            if current_char != targeted_char:
                return False   
            else: 
                board[row][column] = "#"
                char_index += 1
                
            up, right, down, left = False, False, False, False

            # up
            if row - 1 >= 0 and board[row - 1][column] != "#":
                up = helper(row - 1, column, char_index)

            # right
            if column + 1 < columns and board[row][column + 1] != "#":
                right = helper(row, column + 1, char_index)

            # down
            if row + 1 < rows and board[row + 1][column] != "#":
                down = helper(row + 1, column, char_index)

            # left
            if column - 1 >= 0 and board[row][column - 1] != "#":
                left = helper(row, column - 1, char_index)
            
            if (up or right or down or left) == False and char_index != len(word):
                board[row][column] = current_char
                return False
            else:
                return True
        
        for r in range(rows):
            for c in range(columns):
                if helper(r, c, 0):
                    return True
        
        return False