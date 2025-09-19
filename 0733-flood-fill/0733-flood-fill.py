from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original_color = image[sr][sc]
        # mark = []

        # for _ in range(len(image)):
        #     mark.append(["x"] * len(image[0]))

        queue = deque()
        queue.append((sr, sc))
        # mark[sr][sc] = "v"
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # bfs
        while queue:
            sr, sc = queue.popleft()
            
            # update current colour to color if curr colour is the same as original
            if image[sr][sc] == original_color:
                image[sr][sc] = color

            for r, c in directions:
                row = sr + r
                column = sc + c
                

                if 0 <= row < len(image) and 0 <= column < len(image[0]):
                    curr_color = image[row][column]
                    if curr_color != color and curr_color == original_color:
                        # mark[row][column] = "v"
                        queue.append((row, column))

        return image