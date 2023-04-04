class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, position):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            if position == "first":
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            elif position == "last":
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

            else:
                temp_node = self.head
                current_position = 1

                while current_position < position - 1:
                    temp_node = temp_node.next
                    current_position += current_position

                new_node.next = temp_node.next
                new_node.prev = temp_node
                temp_node.next.prev = new_node
                temp_node.next = new_node

    def traverse(self):
        if self.head is None:
            print("Linked List is empty!")

        else:
            temp_node = self.head

            while temp_node is not None:
                print(temp_node.value)
                temp_node = temp_node.next

    def reverse_traverse(self):
        if self.head is None:
            print("Linked List is empty!")

        else:
            temp_node = self.tail

            while temp_node is not None:
                print(temp_node.value)
                temp_node = temp_node.prev

    def delete_node(self, position):
        if self.head is None:
            print("Linked list is empty!")

        else:
            if position == "first":
                if self.head is self.tail:
                    self.head = None
                    self.tail = None

                else:
                    self.head = self.head.next
                    self.head.prev = None

            elif position == "last":
                self.tail = self.tail.prev
                self.tail.next = None

            else:
                temp_node = self.head
                current_position = 1

                while current_position < position - 1:
                    temp_node = temp_node.next
                    current_position += 1

                temp_node.next = temp_node.next.next
                temp_node.next.prev = temp_node

    def delete_entire(self):
        if self.head is None:
            print("linked list is empty!")

        else:
            temp_node = self.head
            while temp_node is not None:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None


doublyll = DoublyLL()
doublyll.insert(1, "last")
doublyll.insert(2, "last")
doublyll.insert(3, "last")
doublyll.insert(4, "last")
doublyll.delete_node(3)
doublyll.traverse()
