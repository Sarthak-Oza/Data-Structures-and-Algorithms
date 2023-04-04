class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
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
                self.head = new_node

            elif position == "append":
                self.tail.next = new_node
                self.tail = new_node

            elif position > 1:
                current_node = self.head
                current_position = 1

                while current_position < position - 1:
                    current_node = current_node.next
                    current_position += 1

                new_node.next = current_node.next
                current_node.next = new_node

            else:
                print("Please enter valid position")

    def traverse(self):
        if self.head is None:
            print("Linked List is empty!")

        else:
            current_node = self.head

            while current_node is not None:
                print(current_node.value)
                current_node = current_node.next

    def search(self, node_value):
        if self.head is None:
            print("Linked List is empty!")

        else:
            current_node = self.head
            while current_node is not None:
                if current_node.value == node_value:
                    print(f"Found the node with value {node_value}")
                    return
                current_node = current_node.next
            print("node does not exist")

    def delete(self, position):
        if self.head is None:
            print("Linked List is empty!")

        else:
            if position == "first":
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                    print(f"first node {self.head.value} deleted!")

                else:
                    self.head = self.head.next
            elif position == "last":
                current_node = self.head

                while current_node.next.next is not None:
                    current_node = current_node.next

                current_node.next = None
                self.tail = None
            else:
                current_node = self.head
                current_position = 1

                while current_position < position - 1:
                    current_node = current_node.next
                print(f"{current_node.next.value} deleted!")
                current_node.next = current_node.next.next


LL = SinglyLinkedList()
LL.insert(1, "append")
LL.insert(2, "append")
LL.insert(3, "append")
LL.delete("last")
LL.traverse()

