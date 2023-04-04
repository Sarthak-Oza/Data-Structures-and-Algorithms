class CircularQueue:
    def __init__(self,max_size):
        self.queue_list = [None] * max_size
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        print_list = [str(i) for i in self.queue_list]
        return "\n".join(print_list)

    def is_full(self):
        if self.start == 0 and self.top + 1 == self.max_size:
            return True
        elif self.start + 1 == self.top:
            return
        else:
            return False

    def is_empty(self):
        if self.start == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.is_full():
            print("The queue is full!")
        else:
            if self.start == -1:
                self.start = 0
                self.top = 0
                self.queue_list[self.top] = value
            elif self.top + 1 == self.max_size:
                self.top = 0
                self.queue_list[self.top] = value
            else:
                self.top += 1
                self.queue_list[self.top] = value

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty!")
        else:
            dequeued_element = self.queue_list[self.start]
            if self.start == self.top:
                self.queue_list[self.start] = None
                self.start = -1
                self.top = -1

            elif self.top + 1 == self.max_size:
                self.queue_list[self.start] = None
                self.start = 0

            else:
                self.queue_list[self.start] = None
                self.start += 1

    def delete_queue(self):
        if self.is_empty():
            print("The queue is empty!")
        else:
            self.queue_list = [None] * self.max_size
            self.start = -1
            self.top = -1


circular_queue = CircularQueue(5)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.enqueue(4)
print(circular_queue)




