class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                pair = stack.pop() if stack else None
                if char == ")":
                    if pair != "(":
                        return False
                elif char == "}":
                    if pair != "{":
                        return False
                else:
                    if pair != "[":
                        return False

        if stack:
            return False
        else:
            return True
                        

