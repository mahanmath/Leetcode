class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []
        self.MyMin = []
    def push(self, x: int) -> None:
        self.L += [x]
        if(self.MyMin):
            m = self.MyMin[-1]
            self.MyMin += [min([m, x])]
        else:
            self.MyMin = [x]
        
    def pop(self) -> None:
        self.L = self.L[:-1]
        self.MyMin = self.MyMin[:-1]
    
    def top(self) -> int:
        return self.L[-1]    

    def getMin(self) -> int:
        return self.MyMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()