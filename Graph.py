from collections import deque

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, value):
        self.graph_dict[value] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
            self.graph_dict[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            self.graph_dict[vertex1].remove(vertex2)
            self.graph_dict[vertex2].remove(vertex1)

    def remove_vertex(self, vertex_val):
        if vertex_val in self.graph_dict:
            for vertex in self.graph_dict[vertex_val]:
                self.graph_dict[vertex].remove(vertex_val)
            del self.graph_dict[vertex_val]

    def bfs(self, vertex):
        visited_vertex_list = []
        queue = deque()
        queue.append(vertex)
        while queue:
            popped_vertex = queue.popleft()
            if popped_vertex not in visited_vertex_list:
                visited_vertex_list.append(popped_vertex)
                for neighbour_vertex in self.graph_dict[popped_vertex]:
                    if neighbour_vertex not in visited_vertex_list:
                        queue.append(neighbour_vertex)
        print(visited_vertex_list)

    def dfs(self, vertex):
        visited_vertex_list = []
        vertex_stack = [vertex]
        while vertex_stack:
            popped_vertex = vertex_stack.pop()
            if popped_vertex not in visited_vertex_list:
                visited_vertex_list.append(popped_vertex)
                for neighbour_vertex in self.graph_dict[popped_vertex]:
                    if neighbour_vertex not in visited_vertex_list:
                        vertex_stack.append(neighbour_vertex)
        print(visited_vertex_list)

    def print_graph(self):
        print(self.graph_dict)


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("C", "E")
graph.add_edge("E", "F")
graph.add_edge("D", "F")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("B", "G")
graph.add_edge("F", "G")
graph.print_graph()
graph.bfs("A")
graph.dfs("A")

