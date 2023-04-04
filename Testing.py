from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BT:
    def __init__(self):
        self.root = None
        print("BT created!")

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            tree_queue = Queue()
            tree_queue.put(self.root)

            while not tree_queue.empty():
                node = tree_queue.get()
                if node.left is None:
                    node.left = new_node
                    return
                else:
                    tree_queue.put(node.left)
                if node.right is None:
                    node.right = new_node
                    return
                else:
                    tree_queue.put(node.right)

    def level_oder_traversal(self):
        if self.root is None:
            print("BT is empty!")
        else:
            tree_queue = Queue()
            tree_queue.put(self.root)

            while not tree_queue.empty():
                node = tree_queue.get()
                print(node.value, end=" -> ")
                if node.left:
                    tree_queue.put(node.left)

                if node.right:
                    tree_queue.put(node.right)

    def find_deepest_delete(self):
        if self.root is None:
            print("BT is empty!")
            return None
        else:
            return_node = None
            tree_queue = Queue()
            tree_queue.put(self.root)
            node = None

            while not tree_queue.empty():
                node = tree_queue.get()
                if node.left:
                    tree_queue.put(node.left)
                if node.right:
                    tree_queue.put(node.right)

            return node

    def delete_deepest_node(self):
        deepest_node_value = self.find_deepest_delete().value
        if deepest_node_value == self.root.value:
            self.root = None
        else:
            tree_queue = Queue()
            tree_queue.put(self.root)

            while not tree_queue.empty():
                node = tree_queue.get()
                if node.left.value == deepest_node_value:
                    node.left = None
                else:
                    tree_queue.put(node.left)
                if node.right.value == deepest_node_value:
                    node.right = None
                else:
                    tree_queue.put(node.right)

    def delete_node(self, value):
        if self.root.value == value:
            self.root = None

        else:
            deepest_node = self.find_deepest_delete().value
            tree_queue = Queue()
            tree_queue.put(self.root)

            while not tree_queue.empty():
                node = tree_queue.get()
                if node.left.value == value:
                    node.left.value = deepest_node.value
                    self.delete_deepest_node()
                    return
                else:
                    tree_queue.put(node.left)
                if node.right.value == value:
                    node.right.value = deepest_node.value
                    self.delete_deepest_node()
                    return
                else:
                    tree_queue.put(node.right)

            print("Value can not be found")

    def depth_first_search(self):
        stack = list()
        stack.append(self.root)
        while stack:
            popped_node = stack.pop()
            print(popped_node.value, end=" ->")
            if popped_node.right:
                stack.append(popped_node.right)
            if popped_node.left:
                stack.append(popped_node.left)

    def breadth_first_search(self):
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            popped_node = queue.get()
            print(popped_node.value, end=" -> ")
            if popped_node.left:
                queue.put(popped_node.left)
            if popped_node.right:
                queue.put(popped_node.right)

    def find_recursively(self, root, target_value):
        if not root:
            return False
        if root.value == target_value:
            return True
        return self.find_recursively(root.left) or self.find_recursively(root.right)

    def sum_of_nodes(self, root):
        if not root:
            return 0
        return root.value + self.sum_of_nodes(root.left) + self.sum_of_nodes(root.right)

    def find_min_node_dfs(self):
        minimum = self.root.value
        stack = list()
        stack.append(self.root)
        while stack:
            popped_node = stack.pop()
            minimum = min(minimum, popped_node.value)
            if popped_node.right:
                stack.append(popped_node.right)
            if popped_node.left:
                stack.append(popped_node.left)
        return minimum

    def no_leaf_nodes(self):
        num = 0
        stack = []
        stack.append(self.root)
        while stack:
            popped_node = stack.pop()
            if popped_node.left or popped_node.right:
                if popped_node.left:
                    stack.append(popped_node.left)
                if popped_node.right:
                    stack.append(popped_node.right)
            else:
                num += 1
        return num


tree = BT()
tree.insert(10)
tree.insert(8)
tree.insert(12)
tree.insert(4)
tree.insert(2)
tree.insert(9)

print(tree.no_leaf_nodes())
