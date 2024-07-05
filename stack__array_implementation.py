class Stack:
    # constructor
    def __init__(self, size):
        self.size = size
        self._stack = [None] * self.size # private variable
        self.top = -1

    # push an item in the stack
    def push(self, value):
        if self.top == self.size - 1:
            return "Overflow"
        else:
            self.top += 1
            self.stack[self.top] = value

    # removes the top item
    def pop(self):
        if self.top == -1:
            return "Empty"
        else:
            data = self.stack[self.top]
            self.top -= 1
            print(data)

    def traverse(self):
        for i in range(self.top + 1):
            print(self.stack[i], end=' ')


s = Stack(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
s.traverse()
# s.push(4)
# print(s.stack)
