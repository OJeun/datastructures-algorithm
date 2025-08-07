class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        reversed_stack = []
        current_str = ''
        current_num = 0

        for char in s:
            if char != ']':
                stack.append(char)
            
            if char == ']':
                popped_char = stack.pop()
                while popped_char != '[':
                    current_str = popped_char + current_str
                    popped_char = stack.pop()

                times = ''
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times

                current_str = current_str * int(times)
                stack.append(current_str)

                current_str = ''     
        
        while stack:
            char = stack.pop()
            current_str = char + current_str
                       
        return current_str
