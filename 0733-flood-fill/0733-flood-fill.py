from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        columns = len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # dfs
        def dfs(curr_r, curr_c):

            for r, c in directions:
                row = curr_r + r
                column = curr_c + c

                if 0 <= row < rows and 0 <= column < columns:
                    if image[row][column] == original_color:
                        image[row][column] = color
                        dfs(row, column)
                        
        image[sr][sc] = color
        dfs(sr, sc)
        return image