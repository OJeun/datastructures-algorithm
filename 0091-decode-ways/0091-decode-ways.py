class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        
        if s[0] == "0":
            return 0
        
        dp[1] = 1
        dp[0] = 1
        
        def helper(digit): # start from 1 to the last digit index
            index = digit - 1

            if digit > len(s):
                return 

            # one digit
            if 0 < int(s[index]):
                dp[digit] += dp[digit - 1] 
            
            # two digit
            if 10 <= int(s[index-1:index+1]) <= 26:
                    dp[digit] += dp[digit-2]

            helper(digit+1)

        helper(2)

        return dp[len(s)]