class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        arithmetic_expression = {
            "+": add, 
            "-": subtract, 
            "*": multiply, 
            "/": divide
            }
        stack = []
        for token in tokens:
            if token not in arithmetic_expression:
                stack.append(int(token))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                result = arithmetic_expression[token](first_operand, second_operand)
                stack.append(result)
        return stack.pop()

    
def add(op1, op2):
    return op1 + op2

def subtract(op1, op2):
    return op1 - op2

def multiply(op1, op2):
    return op1 * op2

def divide(op1, op2):
    return math.trunc(op1 / op2)
