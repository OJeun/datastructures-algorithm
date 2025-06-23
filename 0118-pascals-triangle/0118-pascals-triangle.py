class Solution:
    def generate(self, numRows: int):
        pascalTriangle = []

        for row in range(1, numRows + 1):
            pascalTriangle.append([1] * row)

        for row in range(2, numRows):
            for index in range(1, row):
                prevRow = pascalTriangle[row - 1]
                pascalTriangle[row][index] = prevRow[index - 1] + prevRow[index]

        return pascalTriangle
