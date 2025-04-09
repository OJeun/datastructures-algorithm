class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        temp = [[] for _ in range(numRows)]
        going_up = True
        row = 0

        for i in range(len(s)):
            if row == numRows - 1:
                going_up = False
                
            if row == 0:
                going_up = True

            temp[row].append(s[i])

            if going_up:
                row += 1
            else:
                row -= 1

        result = ""
        for row in temp:
            result += "".join(row)

        return result