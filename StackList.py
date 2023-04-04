class Stack:
    def __init__(self, max_limit):
        self.list = []
        self.max_limit = max_limit

    def __str__(self):
        reverse_str = self.list.reverse()
        reverse_str = [str(i) for i in self.list]
        return "\n".join(reverse_str)

    def is_empty(self):
        if not self.list:
            return True
        else:
            return False

    def is_full(self):
        if len(self.list) == self.max_limit:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            print("Stack is full!")
        else:
            self.list.append(value)
            print("Value entered!")

    def pop(self):
        if self.is_empty():
            return "The stack is empty!"
        else:
            self.list.pop()
            return "The element has been popped!"

    def peek(self):
        if self.is_empty():
            return "The stack is empty!"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        if self.is_empty():
            print("The stack is already empty!")
            return
        else:
            self.list = None
            print("The stack deleted!")


new_stack = Stack(5)
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.pop()
print(new_stack.peek())
print(new_stack)

