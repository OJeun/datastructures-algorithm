class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        layers = len(matrix) // 2
        n = len(matrix)

        for layer in range(layers):
            first = layer
            last = n - layer - 1
            for i in range(first, last): # 0 - 2

                offset = i - first
                top = matrix[first][i] # (0, 0)

                # left to top
                matrix[first][i] = matrix[last - offset][first]

                # bottom to left
                matrix[last-offset][first] = matrix[last][last-offset]

                # right to bottom
                matrix[last][last-offset] = matrix[i][last]

                # top -> right
                matrix[i][last] = top

            
