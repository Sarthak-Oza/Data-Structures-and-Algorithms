class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        if self.linked_list is None:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linked_list.head
        self.linked_list.head = new_node

    def traverse(self):
        temp_node = self.linked_list.head

        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return
        else:
            return self.linked_list.head.value

    def pop(self):
        popped_value = self.linked_list.head.value
        self.linked_list.head = self.linked_list.head.next
        return popped_value


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.traverse()
print(stack.peek())
print(stack.pop())
