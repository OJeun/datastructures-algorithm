class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        result = 0
        symbol_pointer = 0 

        while symbol_pointer < len(s):
            if symbol_pointer + 1 < len(s) and symbol_dict[s[symbol_pointer + 1]] > symbol_dict[s[symbol_pointer]]:
                result += (symbol_dict[s[symbol_pointer + 1]] - symbol_dict[s[symbol_pointer]])
                symbol_pointer += 1
                
            else:
                result += symbol_dict[s[symbol_pointer]]

            symbol_pointer += 1
        return result
        

