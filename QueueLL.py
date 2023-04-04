class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Queue:
    def __init__(self):
        self.queue_linkedlist = LinkedList()

    def enqueue(self, value):
        new_node = Node(value)
        if self.queue_linkedlist.head is None:
            self.queue_linkedlist.head = new_node
            self.queue_linkedlist.tail = new_node
        else:
            self.queue_linkedlist.tail.next = new_node
            self.queue_linkedlist.tail = new_node

    def dequeue(self):
        if self.queue_linkedlist.head is None:
            print("Queue is empty!")
        else:
            if self.queue_linkedlist.head is self.queue_linkedlist.tail:
                self.queue_linkedlist.head = None
                self.queue_linkedlist.tail = None

            else:
                self.queue_linkedlist.head = self.queue_linkedlist.head.next

    def peek(self):
        if self.queue_linkedlist.head is None:
            print("The queue is empty!")
        else:
            return self.queue_linkedlist.head.value

    def delete_queue(self):
        if self.queue_linkedlist.head is None:
            print("The queue is empty!")
        else:
            self.queue_linkedlist.head = None
            self.queue_linkedlist.tail = None
