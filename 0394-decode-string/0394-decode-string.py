class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ""
        times = ""

        i = len(s) - 1
        
        while i >= 0:
            char = s[i]

            if char == "[":
                subString = ""
                sub_c = stack.pop()
                while sub_c != "]":
                    subString = subString + sub_c
                    sub_c = stack.pop()
                stack.append(subString)
                i -= 1

            elif char.isdigit():
                while char.isdigit():
                    times = char + times
                    i -= 1
                    char = s[i]
                chars_in_bracket = stack.pop()
                stack.append(chars_in_bracket * int(times))
                times = ""
                
            else:
                stack.append(char)
                i -= 1

        while stack:
            char = stack.pop()
            result = result + char
                
        return result
            