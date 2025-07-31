class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        for r in range(rows):
            for l in range(columns):
                if matrix[r][l] == 0:
                    # up
                    row = r - 1
                    while row >= 0:
                        if matrix[row][l] != 0:
                            matrix[row][l] = 'v'
                        row -= 1

                    # down
                    row = r + 1
                    while row < rows:
                        if matrix[row][l] != 0:
                            matrix[row][l] = 'v'
                        row += 1

                    # left
                    column = l - 1
                    while column >= 0:
                        if matrix[r][column] != 0:
                            matrix[r][column] = 'v'
                        column -= 1

                    # right
                    column = l + 1
                    while column < columns:
                        if matrix[r][column] != 0:
                            matrix[r][column] = 'v'                       
                        column += 1

        for r in range(rows):
            for l in range(columns):
                if matrix[r][l] == 'v':
                    matrix[r][l] = 0