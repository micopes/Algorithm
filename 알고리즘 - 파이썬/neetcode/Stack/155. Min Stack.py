class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [] 
    def push(self, val: int) -> None:
        self.stack.append(val)
        # 스택의 최솟값이 min_stack[-1] 시 조회되도록
        if len(self.min_stack) == 0 or self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1]) # 이전 값과 비교해서 최소인 것.......이 있음.
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.min_stack.pop()
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.min_stack[-1]
