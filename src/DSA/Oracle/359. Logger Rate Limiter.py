class Logger:

    def __init__(self):
        self.msgTracker = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.msgTracker:
            self.msgTracker[message] = timestamp
            return True
        
        if timestamp - self.msgTracker[message] <= 9:
            return False
        
        self.msgTracker[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
obj = Logger()
print(obj.shouldPrintMessage(1, 'foo'))
print(obj.shouldPrintMessage(2, 'bar'))
print(obj.shouldPrintMessage(3, 'foo'))
print(obj.shouldPrintMessage(8, 'bar'))
print(obj.shouldPrintMessage(10, 'foo'))
print(obj.shouldPrintMessage(11, 'foo'))