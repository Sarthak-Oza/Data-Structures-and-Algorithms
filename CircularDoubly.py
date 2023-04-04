class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyCircular:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,value,position):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head

        else:
            if position == "prepand":
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = self.head

            elif position == "append":
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                self.tail.next = self.head

            else:
                temp_node = self.head
                current_position = 1

                while current_position < position-1:
                    temp_node = temp_node.next
                    current_position += current_position

                new_node.next = temp_node.next
                temp_node.next = new_node
                new_node.prev = temp_node
                new_node.next.prev = new_node

    def traverse(self):
        if self.head is None:
            print("Linked List is empty!")

        else:
            temp_node = self.head

            while True:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node is self.head:
                    break

    def reverse_traverse(self):
        if self.head is None:
            print("Linked list is empty!")
            return
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
                self.head.next.prev = None
                self.head = self.head.next
                self.tail.next = self.head

            elif position == "last":
                self.tail.prev.next = self.head
                self.tail = self.tail.prev

            else:
                temp_node = self.head
                current_position = 1

                while current_position < position-1:
                    temp_node = temp_node.next
                    current_position += current_position

                temp_node.next.next.prev = temp_node
                temp_node.next = temp_node.next.next





doubly_circular = DoublyCircular()
doubly_circular.insert(1,"prepend")
doubly_circular.insert(4,"append")
doubly_circular.insert(2,2)
doubly_circular.insert(3,3)
doubly_circular.insert(5,"append")
doubly_circular.delete_node(3)

doubly_circular.reverse_traverse()