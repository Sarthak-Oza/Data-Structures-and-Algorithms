class BinaryTree:
    def __init__(self,size):
        self.tree_list = size * [None]
        self.max_size = size
        self.last_used_index = 0

    def insert(self,value):
        if self.max_size == self.last_used_index+1:
            print("List is full!")
            return
        else:
            self.tree_list[self.last_used_index+1] = value
            self.last_used_index += 1
            print(f"{value} entered!")

    def level_order_traversal(self):
        if self.last_used_index == 0:
            print("The tree is empty!")
            return
        else:
            for i in range(1, self.last_used_index+1):
                print(self.tree_list[i])

    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return

        print(self.tree_list[index])
        self.pre_order_traversal(2*index)
        self.pre_order_traversal((2*index + 1))

    def in_order_traversal(self,index):
        if index > self.last_used_index:
            return

        self.in_order_traversal(2*index)
        print(self.tree_list[index])
        self.in_order_traversal(2*index + 1)

    def search_node(self,value):
        for i in range(1, self.last_used_index+1):
            if self.tree_list[i] == value:
                print("found")
                return
        print("Not found!")

    def delete_node(self,value):
        for i in range(1, self.last_used_index+1):
            if self.tree_list[i] == value:
                deepest_node = self.tree_list[self.last_used_index]
                self.tree_list[self.last_used_index] = None
                self.tree_list[i] = deepest_node
                self.last_used_index -= 1
                return

        print("Not found")

    def delete_tree(self):
        self.tree_list = None
        print("tree deleted")


binary_tree = BinaryTree(10)
binary_tree.insert(1)
binary_tree.insert(2)
binary_tree.insert(3)
binary_tree.insert(4)
binary_tree.insert(5)
binary_tree.insert(6)
binary_tree.insert(7)
binary_tree.pre_order_traversal(1)
binary_tree.search_node(10)
binary_tree.delete_node(3)
binary_tree.level_order_traversal()
