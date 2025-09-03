class MyQueue:
    def __init__(self):
        self.stack = []
        self.reversed_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.reversed_stack:
            for _ in range(len(self.stack)):
                self.reversed_stack.append(self.stack.pop())

        return self.reversed_stack.pop()

    def peek(self) -> int:
        if self.reversed_stack:
            return self.reversed_stack[-1]
        else:
            return self.stack[0]

    def empty(self) -> bool:
        if self.stack or self.reversed_stack:
            return False
        else:
            return True
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()