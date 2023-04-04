class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        str_list = [str(i) for i in self.list]
        return "\n".join(str_list)

    def is_empty(self):
        if not self.list:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)
        print(f"value {value} entered!")

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty!")
            return
        else:
            return self.list.pop(0)

    def peek(self):
        if self.is_empty():
            print("The queue is empty")
        else:
            return self.list[0]

    def delete_queue(self):
        if self.is_empty():
            print("The queue is already empty!")
        else:
            self.list = None
            print("The queue deleted!")


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.peek()
print(queue)