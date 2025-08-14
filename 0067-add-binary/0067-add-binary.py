class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        carry = 0
        result = ""

        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord("0") if i < len(a) else 0
            digit_b = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digit_a + digit_b + carry

            result = str(total % 2) + result
            carry = total // 2

        if carry == 1:
            result = "1" + result

        return result


            

