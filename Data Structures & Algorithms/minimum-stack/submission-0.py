class MinStack:

    def __init__(self):
        self.stack = []   

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))     # adding to the stack as a tuple, where (val, minimum val so far)
        else:
            prevMin = self.stack[-1][1]
            self.stack.append((val, min(val, prevMin)))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
