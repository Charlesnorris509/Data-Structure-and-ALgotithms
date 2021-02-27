"""This is the code for a stack datastructure implementation
@Charles Norris  26/2/2021"""

class Stack:

    def __init__(self, data):
        self.data = data

    def is_Empty(self):
        return self.stack == []

    def push(self):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

stack = Stack()
stack.push(3)
stack.push(5)
stack.push(1)
stack.push(10)
print(stack.sizeStack())
print('Peek :', stack.peek())
    