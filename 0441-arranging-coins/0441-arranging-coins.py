class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        memoization = [0]
        coins = 0

        while coins <= n:
            prev = rows
            next_row = memoization[prev] + 1
            coins += next_row
            if coins <= n:
                memoization.append(memoization[prev] + 1)
                rows += 1

        return rows
    