from queue import Queue


class Graph:
    def __init__(self):
        self.graph_dict = {}
        print("Graph created")

    def graph_print(self):
        print(self.graph_dict)

    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            print("Vertex is already present in the graph")
            return
        else:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            if vertex2 not in self.graph_dict[vertex1]:
                self.graph_dict[vertex1].append(vertex2)
            if vertex1 not in self.graph_dict[vertex2]:
                self.graph_dict[vertex2].append(vertex1)
        else:
            print("Vertex not present in graph")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            if vertex2 in self.graph_dict[vertex1]:
                self.graph_dict[vertex1].remove(vertex2)
            if vertex1 in self.graph_dict[vertex2]:
                self.graph_dict[vertex2].remove(vertex1)
        else:
            print("Edge does not exist")

    def remove_vertex(self, vertex):
        if vertex in self.graph_dict:
            for other_vertex in self.graph_dict[vertex]:
                self.graph_dict[other_vertex].remove(vertex)

        del self.graph_dict[vertex]

    def delete_graph(self):
        self.graph_dict.clear()

    def bfs(self, graph1, start_node):
        bfs_queue = Queue()
        visited_node = []
        bfs_queue.put(start_node)
        while not bfs_queue.empty():
            dequeue_node = bfs_queue.get()
            if dequeue_node not in visited_node:
                visited_node.append(dequeue_node)
                for node in self.graph_dict[dequeue_node]:
                    if node not in visited_node:
                        bfs_queue.put(node)

        print(visited_node)
        return

    def dfs(self, graph1, start_node):
        dfs_stack = [start_node]
        visited_node = []
        while dfs_stack:
            print(dfs_stack)
            popped_node = dfs_stack.pop()
            if popped_node not in visited_node:
                visited_node.append(popped_node)
                for node in self.graph_dict[popped_node]:
                    if node not in visited_node:
                        dfs_stack.append(node)

        print(visited_node)
        return


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "A")
graph.add_edge("B", "E")
graph.add_edge("C", "A")
graph.add_edge("C", "D")
graph.add_edge("D", "C")
graph.add_edge("D", "E")
graph.add_edge("E", "B")
graph.add_edge("E", "D")
# graph.remove_vertex("E")
graph.bfs(graph.graph_dict, "A")
graph.dfs(graph.graph_dict, "A")
graph.delete_graph()


# graph.graph_print()
