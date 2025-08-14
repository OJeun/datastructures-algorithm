class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = []
        self.count = 0
        for _ in range(len(s)):
            dp.append([-1] * len(s))
        
        for i in range(len(s)):
            dp[i][i] = True

        def recursive(start, end) -> bool:
            if dp[start][end] != -1:
                return dp[start][end]

            if start > end:
                return True

            if s[start] == s[end] and recursive(start+1, end-1):
                dp[start][end] = True
                self.count += 1
                return True

            dp[start][end] = False
                

        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] == -1:
                    recursive(i, j)

        return self.count + len(s)


        