class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0
     
  
# Create a new stack
stack1 = Stack()

# Push elements onto the stack
stack1.push(1)
stack1.push(2)
stack1.push(3)

# Check if the stack is empty
print(stack1.isEmpty())  # False

# Pop elements from the stack
print(stack1.pop())  # 3
print(stack1.pop())  # 2
print(stack1.pop())  # 10
print(stack1.pop())  # None

# Check if the stack is empty again
print(stack1.isEmpty())  # True