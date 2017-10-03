
def find_unvisited_edge(node):
    for e in node.out_edges:
        if not e.visited:
            return e
    return None


def find_cycle(graph):
    temp_path = []
    final_path = []

    # Start at any node
    cur_node = graph.values()[0]

    # Keep walking until we can't walk anymore
    while cur_node is not None:
        edge = find_unvisited_edge(cur_node)
        if edge is not None:
            temp_path.append(cur_node)
            cur_node = edge.tail
            edge.visited = True
        else:
            final_path.append(cur_node)
            if len(temp_path) > 0:
                cur_node = temp_path.pop()
            else:
                cur_node = None

    return list(reversed(final_path))


def format_path(path):
    str = ""
    for n in path:
        if len(str) > 0:
            str += "->"
        str += n.label
    return str
