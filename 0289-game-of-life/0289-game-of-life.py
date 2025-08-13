class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        encoding = {
            "d": 1, # currently died, but reproduction
            "a": 0, # currently alive, but will die 
        }

        for r in range(rows):
            for l in range(columns):
                alive = 0
                dead = 0
                for r_offset, l_offset in directions:
                    moved_r = r + r_offset
                    moved_l = l + l_offset

                    if moved_r < 0 or moved_l < 0 or moved_r >= rows or moved_l >= columns:
                        continue
                    else:
                        neighbor = board[moved_r][moved_l]
                        if neighbor == 0 or neighbor == "d":
                            dead += 1
                        else:
                            alive += 1

                if board[r][l] == 1:
                    if alive < 2 or alive > 3:
                        board[r][l] = "a"
                else:
                    if alive == 3:
                        board[r][l] = "d"


        for r in range(rows):
            for l in range(columns):
                cell = board[r][l]
                if cell == "a":
                    board[r][l] = 0
                elif cell == "d":
                    board[r][l] = 1




