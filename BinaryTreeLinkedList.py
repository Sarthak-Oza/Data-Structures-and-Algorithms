from queue import Queue


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def pre_order_traversal(root_node):
    if not root_node:
        return

    print(root_node.value)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_oder_traversal(root_node):
    if not root_node:
        return

    in_oder_traversal(root_node.left_child)
    print(root_node.value)
    in_oder_traversal(root_node.right_child)


def post_order_traversal(root_node):
    if not root_node:
        return

    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.value)


def level_order_traversal(root_node):
    if root_node is None:
        return

    tree_queue = Queue()
    tree_queue.put(root_node)

    while not tree_queue.empty():
        root_node = tree_queue.get()
        print(root_node.value)

        if root_node.left_child is not None:
            tree_queue.put(root_node.left_child)

        if root_node.right_child is not None:
            tree_queue.put(root_node.right_child)


def add_node(root_node, new_node):
    if root_node is None:
        root_node = new_node

    else:
        tree_queue = Queue()
        tree_queue.put(root_node)

        while not tree_queue.empty():
            node = tree_queue.get()

            if node.left_child is None:
                node.left_child = new_node
                print(f"{node.value} entered!")
                return
            else:
                tree_queue.put(node.left_child)

            if node.right_child is None:
                node.right_child = new_node
                print(f"{node.value} entered!")
                return
            else:
                tree_queue.put(node.right_child)


def search_node(root_node, node_value):
    if root_node.value == node_value:
        print("Found it!")
        return
    else:
        tree_queue = Queue()
        tree_queue.put(root_node)

        while not tree_queue.empty():
            node = tree_queue.get()

            if node.left_child:
                if node.left_child.value == node_value:
                    print("Found")
                    return
                else:
                    tree_queue.put(node.left_child)

            if node.right_child:
                if node.right_child.value == node_value:
                    print("Found")
                    return
                else:
                    tree_queue.put(node.right_child)
        print("Not found!!")


def find_deepest_node(root_node):
    if not root_node:
        print("Root node does not exist")
        return

    tree_queue = Queue()
    tree_queue.put(root_node)
    node = None
    while not tree_queue.empty():
        node = tree_queue.get()

        if node.left_child:
            tree_queue.put(node.left_child)

        if node.right_child:
            tree_queue.put(node.right_child)
    return node


def delete_deepest_node(root_node):
    if root_node is find_deepest_node(root_node):
        print("root node is the deepest node, deleting!")
        root_node = None
        return
    else:
        tree_queue = Queue()
        tree_queue.put(root_node)

        while not tree_queue.empty():
            node = tree_queue.get()

            if node.left_child is find_deepest_node(root_node):
                node.left_child = None
                print("Node deleted!")
                return
            else:
                tree_queue.put(node.left_child)

            if node.right_child is find_deepest_node(root_node):
                node.right_child = None
                print("\nNode deleted!")
                return
            else:
                tree_queue.put(node.right_child)


def delete_node(root_node, node_value):
    if root_node.value == node_value:
        root_node.value = find_deepest_node(root_node).value
        delete_deepest_node(root_node)
        print("Root node was the node, replaced the value with the deepest node and deleted the deepest node!")

    else:

        tree_queue = Queue()
        tree_queue.put(root_node)

        while not tree_queue.empty():
            node = tree_queue.get()

            if node.left_child.value == node_value:
                node.left_child.value = find_deepest_node(root_node).value
                delete_deepest_node(root_node)
                print("Node deleted and replaced")
                return
            else:
                tree_queue.put(node.left_child)

            if node.right_child.value == node_value:
                node.right_child.value = find_deepest_node(root_node).value
                delete_deepest_node(root_node)
                print("Node deleted and replaced")
                return
            else:
                tree_queue.put(node.right_child)

        print("Not found!")


def delete_tree(root_node):
    root_node.value = None
    root_node.left_child = None
    root_node.right_child = None


new_node = TreeNode("Drinks")
new_node.left_child = TreeNode("Hot")
new_node.right_child = TreeNode("Cold")
add_node(new_node, TreeNode("Coffee"))
add_node(new_node, TreeNode("Tea"))
level_order_traversal(new_node)

level_order_traversal(new_node)
delete_node(new_node, "Coffee")
level_order_traversal(new_node)
delete_tree(new_node)
level_order_traversal(new_node)
