class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root_node = Node(None)
        print("BST created!!")

    def pre_oder_traversal(self, root_node):
        if self.root_node is None:
            print("BST is empty!")
            return
        else:
            if root_node is None:
                return

            print(root_node.value)
            self.pre_oder_traversal(root_node.left_child)
            self.pre_oder_traversal(root_node.right_child)

    def insert_node(self, root_node, value):
        new_node = Node(value)

        if self.root_node is None:
            self.root_node = new_node
            print("New node entered as root node")
            return

        else:
            if value < root_node.value:
                if root_node.left_child:
                    self.insert_node(root_node.left_child, value)
                else:
                    root_node.left_child = new_node
                    print("Node entered!")
                    return
            if value > root_node.value:
                if root_node.right_child:
                    self.insert_node(root_node.right_child, value)
                else:
                    root_node.right_child = new_node
                    print("Node entered!")
                    return

    def delete_node(self, root_node, node_value):
        if not root_node:
            return
        elif node_value < root_node.value:

            if root_node.left_child:
                root_node.left_child = self.delete_node(root_node.left_child, node_value)
            else:
                print("The node does not exist")
                return
        elif node_value > root_node.value:
            if root_node.right_child:
                root_node.right_child = self.delete_node(root_node.right_child, node_value)
            else:
                print("The node does not exist")

        else:

            if root_node.left_child is None:
                temp = root_node.right_child
                root_node.right_child = None
                return temp

            if root_node.right_child is None:
                temp = root_node.left_child
                root_node.left_child = None
                return temp

            node = root_node.right_child
            while node.left_child:
                node = node.left_child

            return node


bst = BinarySearchTree()
bst.root_node.value = 10
bst.insert_node(bst.root_node, 8)
bst.insert_node(bst.root_node, 6)
bst.insert_node(bst.root_node, 12)
bst.insert_node(bst.root_node, 20)
bst.delete_node(bst.root_node, 8)
bst.pre_oder_traversal(bst.root_node)




------------------------------------------------------------------------------------



class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root_node = Node(None)
        print("BST with empty node created!")

    def pre_order_traversal(self,root_node):
        if root_node is None:
            print("BST empty!")
            return
        else:
            if root_node is None:
                return

            print(root_node.value)
            self.pre_order_traversal(root_node.left_child)
            self.pre_order_traversal(root_node.right_child)

    def insert_node(self,root_node, node_value):
        if root_node is None:
            root_node.value = node_value
            return
        elif node_value < root_node.value:
            if self.root_node.left_child:
                self.insert_node(root_node.left_child)
            else:
                self.root_node.left_child = Node(node_value)
                print(self.root_node.left_child.value)
                print(f"Node with value {node_value} entered as a left child node!!")
                return
        elif node_value > root_node.value:
            if self.root_node.right_child:
                self.insert_node(root_node.right_child)
            else:
                self.root_node.right_child = Node(node_value)
                print(f"Node with value {node_value} entered as a right child node!!")
                return

    def delete_node(self,root_node,node_value):
        if not self.root_node:
            print("BST is empty!")
            return
        else:
            if node_value < root_node.value:
                if root_node.left_child:
                    root_node.left_child = self.delete_node(root_node.left_child, node_value)
                else:
                    print("The node does not exist")
                    return

            if node_value > root_node.value:
                if root_node.right_child:
                    root_node.right_child = self.delete_node(root_node.right_child, node_value)
                else:
                    print("The node does not exist")
                    return

            if root_node.left_child is None:
                temp = root_node.right_child
                root_node.right_child = None
                return temp
            if root_node.right_child is None:
                temp = root_node.left_child
                root_node.left_child = None
                return temp

            node = root_node.right_child
            while root_node.left_child:
                root_node = root_node.left_child

            return node


bst = BinarySearchTree()
bst.root_node.value = 10
bst.insert_node(bst.root_node, 5)
bst.insert_node(bst.root_node, 15)
print(bst.root_node.left_child.value)