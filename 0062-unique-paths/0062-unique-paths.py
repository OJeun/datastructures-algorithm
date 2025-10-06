class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memoization = []
        # columns = n
        # rows = m

        for _ in range(m):
            self.memoization.append([-1] * n)

        for c in range(n):
            self.memoization[0][c] = 1

        for r in range(m):
            self.memoization[r][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                pair_sum = self.memoization[r-1][c] + self.memoization[r][c-1]
                self.memoization[r][c] = pair_sum

        return self.memoization[m-1][n-1]