class Solution:
    def addBinary(self, a: str, b: str) -> str:
        point_a = len(a) - 1
        point_b = len(b) - 1
        carry = 0
        result = ""

        while point_a >= 0 and point_b >= 0:
            add_two = int(a[point_a]) + int(b[point_b]) + carry
            carry = add_two // 2
            result = str(add_two % 2) + result 
            point_a -= 1
            point_b -= 1

        binary, pointer = (a, point_a) if point_a >= 0 else (b, point_b)

        while pointer >= 0:
            add_two = int(binary[pointer]) + carry 
            carry = add_two // 2
            result = str(add_two % 2) + result

            pointer -= 1

        if carry == 1:
            result = "1" + result

        return result


            

