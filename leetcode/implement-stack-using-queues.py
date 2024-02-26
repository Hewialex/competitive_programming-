class MyStack:

    def __init__(self):
        self.s = deque()
        

    def push(self, x: int) -> None:
        self.s.append(x)
        

    def pop(self) -> int:
        return self.s.pop()

        

    def top(self) -> int:
        return self.s[-1]
        

    def empty(self) -> bool:
        if len(self.s) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()