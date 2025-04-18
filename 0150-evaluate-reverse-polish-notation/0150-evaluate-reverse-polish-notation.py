class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        arithmetic_expression = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b)
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

