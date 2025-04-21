class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0      # 현재까지의 누적 결과
        sign = 1        # 현재 부호: +1 또는 -1
        num = 0         # 현재 파싱 중인 숫자

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # 여러 자리 숫자 처리
            elif char == "+":
                result += sign * num
                num = 0
                sign = 1
            elif char == "-":
                result += sign * num
                num = 0
                sign = -1
            elif char == "(":
                # 현재 계산 상태를 저장
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num  # 괄호 내부 계산 마무리
                num = 0
                result *= stack.pop()    # 앞의 부호
                result += stack.pop()    # 앞의 결과값
            # 공백은 무시

        return result + sign * num  # 마지막 숫자 처리
