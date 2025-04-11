class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n - 1

        while start < end:
            while start < n and not s[start].isalpha() and not s[start].isnumeric():
                start += 1
            while end > -1 and not s[end].isalpha() and not s[end].isnumeric():
                end -= 1
            
            if start > n - 1 and end < 0:
                return True
            
            if s[start].lower() != s[end].lower():
                return False
                
            start += 1
            end -= 1

        return True