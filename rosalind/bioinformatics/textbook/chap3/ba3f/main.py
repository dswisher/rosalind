
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn


def find_unvisited_edge(node):
    for e in node.out_edges:
        if not e.visited:
            return e
    return None


def find_eulerian_cycle(graph):
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


def main(fname):
    with open(util.find_file(sys.argv[1]), "r") as fp:
        graph = debruijn.read_adjacency_list(fp)

    path = find_eulerian_cycle(graph)
    print format_path(path)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
