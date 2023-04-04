class BinaryHeap:
    def __init__(self, max_size):
        self.heap_list = (max_size + 1) * [None]
        self.heap_size = 0
        self.max_size = max_size
        print("Binary heap tree created!")

    def size_heap(self):
        return self.heap_size

    def peek(self):
        if self.heap_size == 0:
            print("Binary heap is empty!")
            return
        else:
            return self.heap_list[self.heap_size]

    def level_order_traversal(self):
        if self.heap_size == 0:
            print("Binary heap is empty!")
            return
        else:
            for i in range(1, self.heap_size + 1):
                print(self.heap_list[i])

    def heapify(self, heap_type, index):
        if index <= 1:
            return
        else:
            parent_index = int(index / 2)

            if heap_type == "Min":
                if self.heap_list[index] < self.heap_list[parent_index]:
                    temp = self.heap_list[index]
                    self.heap_list[index] = self.heap_list[parent_index]
                    self.heap_list[parent_index]
                    self.heapify("Min", parent_index)

            if heap_type == "Max":
                if self.heap_list[index] > self.heap_list[parent_index]:
                    temp = self.heap_list[index]
                    self.heap_list[index] = self.heap_list[parent_index]
                    self.heap_list[parent_index]
                    self.heapify("Max", parent_index)

    def insert_node(self, node_value, heap_type):
        self.heap_list[self.heap_size + 1] = node_value
        self.heap_size += 1
        self.heapify(heap_type, self.heap_size)

    def heapify_tree_extract(self, root_index, heap_type):
        left_child_index = root_index * 2
        right_child_index = (root_index * 2) + 1
        swap_index = 0
        if left_child_index > self.heap_size:
            return

        elif left_child_index == self.heap_size:
            if heap_type == "Min":
                if self.heap_list[left_child_index] < self.heap_list[root_index]:
                    temp = self.heap_list[left_child_index]
                    self.heap_list[left_child_index] = self.heap_list[root_index]
                    self.heap_list[root_index] = temp
                    return

            if heap_type == "Max":
                if self.heap_list[left_child_index] > self.heap_list[root_index]:
                    temp = self.heap_list[left_child_index]
                    self.heap_list[left_child_index] = self.heap_list[root_index]
                    self.heap_list[root_index] = temp
                    return

        else:
            if heap_type == "Min":
                if self.heap_list[left_child_index] < self.heap_list[right_child_index]:
                    swap_index = left_child_index
                else:
                    swap_index = right_child_index

                if self.heap_list[swap_index] < self.heap_list[root_index]:
                    temp = self.heap_list[swap_index]
                    self.heap_list[swap_index] = self.heap_list[root_index]
                    self.heap_list[root_index] = temp

            if heap_type == "Max":
                if self.heap_list[left_child_index] < self.heap_list[right_child_index]:
                    swap_index = right_child_index
                else:
                    swap_index = left_child_index

                if self.heap_list[swap_index] > self.heap_list[root_index]:
                    temp = self.heap_list[swap_index]
                    self.heap_list[swap_index] = self.heap_list[root_index]
                    self.heap_list[root_index] = temp

            self.heapify_tree_extract(swap_index, heap_type)

    def extract_node(self, heap_type):
        if self.heap_size == 0:
            print("Binary heap is empty!")
            return
        else:
            extracted_node = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.heap_size]
            self.heap_list[self.heap_size] = None
            self.heap_size -= 1
            self.heapify_tree_extract(1, heap_type)
            return extracted_node


binary_heap = BinaryHeap(10)
binary_heap.insert_node(1, "Min")
binary_heap.insert_node(2, "Min")
binary_heap.insert_node(3, "Min")
binary_heap.insert_node(4, "Min")
binary_heap.extract_node("Min")
binary_heap.extract_node("Min")
binary_heap.level_order_traversal()
