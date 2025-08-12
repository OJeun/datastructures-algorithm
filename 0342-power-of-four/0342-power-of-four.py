class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        log_val = math.log(n, 4)
        return log_val.is_integer()
            

