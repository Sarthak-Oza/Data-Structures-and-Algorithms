from collections import defaultdict


def create_graph(edges):
    graph_dict = defaultdict(list)

    for edge in edges:
        graph_dict[edge[0]].append(edge[1])

    return graph_dict


print(create_graph([
    ["A", "B"], ["A", "C"],
    ["B", "A"], ["B", "D"],
    ["C", "A"], ["C", "D"], ["C", "E"],
    ["D", "C"], ["D", "B"], ["D", "F"],
    ["E", "C"], ["E", "F"],
    ["F", "E"], ["F", "D"], ["F", "G"]
]))

def sssp_bfs(graph_dict, start, end):
    if start == end:
        return start

    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:

            for neighbour in graph_dict[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end:
                    return new_path

            visited.append(node)

    return "Path to destination does not exist!"


sssp_bfs(create_graph([
    ["A", "B"], ["A", "C"],
    ["B", "A"], ["B", "D"],
    ["C", "A"], ["C", "D"], ["C", "E"],
    ["D", "C"], ["D", "B"], ["D", "F"],
    ["E", "C"], ["E", "F"],
    ["F", "E"], ["F", "D"], ["F", "G"]
]), "A", "F")

