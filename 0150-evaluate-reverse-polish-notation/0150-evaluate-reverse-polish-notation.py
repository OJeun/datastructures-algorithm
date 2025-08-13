class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:

            if token in operators:
                result = 0
                second_operand = stack.pop()
                first_operand = stack.pop()

                if token == "*":
                    result = first_operand * second_operand

                elif token == "/":
                    result = int(first_operand / second_operand)

                elif token == "+":
                    result = first_operand + second_operand

                else:
                    result = first_operand - second_operand
                
                stack.append(result)

            else:
                stack.append(int(token))

        
        return stack.pop()