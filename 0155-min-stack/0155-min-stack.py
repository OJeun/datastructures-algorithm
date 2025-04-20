class MinStack:

    def __init__(self):
        self.stack = []
        self.min = math.inf
        self.second_min = math.inf
        self.min_stack = [self.min]

    def push(self, val: int) -> None:
        if val <= self.min:
            self.second_min = self.min
            self.min = min(self.min, val)
            self.min_stack[0] = self.min
            
        if val > self.min and val < self.second_min:
            self.second_min = val

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[0]:
                self.min_stack[0] = self.second_min
        else:
            return None
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min_stack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()