class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyCircularLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, position):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head

        elif position == "prepend":
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

        elif position == "append":
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        else:
            temp_node = self.head
            current_position = 1

            while current_position < position - 1:
                temp_node = temp_node.next
                current_position += current_position

            new_node.next = temp_node.next
            temp_node.next = new_node

    def traverse(self):
        if self.head is None:
            print("Singly circular linked list is empty!")

        else:
            temp_node = self.head
            print(temp_node.value)
            while temp_node.next is not self.head:
                temp_node = temp_node.next
                print(temp_node.value)

    def delete(self, position):
        if self.head is None:
            print("Linked list does not exist!")
        else:
            if position == "first":
                if self.head is self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif position == "last":
                if self.head is self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    temp_node = self.head

                    while temp_node.next.next is not self.head:
                        temp_node = temp_node.next

                    temp_node.next = self.head
                    self.tail = temp_node

            else:
                temp_node = self.head
                current_position = 1

                while current_position < position - 1:
                    temp_node = temp_node.next
                    current_position += 1

                temp_node.next = temp_node.next.next

    def search(self, value):
        if self.head is None:
            print("Linked list is empty!")
        else:
            temp_node = self.head
            if self.head.value == value:
                print("found")
                return
            temp_node = temp_node.next
            while temp_node is not self.head:
                if temp_node.value == value:
                    print("found")
                    return
                temp_node = temp_node.next
        print("not found")
        return

    def delete_ll(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            self.tail.next = None
            self.head = None
            self.tail = None


singly_circular_LL = SinglyCircularLL()
singly_circular_LL.insert(1, "append")
singly_circular_LL.insert(2, "append")
singly_circular_LL.insert(3, "append")
singly_circular_LL.delete_ll()
singly_circular_LL.traverse()
singly_circular_LL.search(7)
