
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn


def search(visited, node):
    if node.label not in visited:
        visited.add(node.label)
        for e in node.out_edges:
            search(visited, e.tail)
        for e in node.in_edges:
            search(visited, e.head)


def main(fname):
    # Read in the graph
    with open(util.find_file(fname), "r") as fp:
        node_dict = debruijn.read_edge_list(fp)

    # Set up a set to keep track of the nodes that have been visited
    visited = set()

    # Set up a queue of all nodes
    queue = []
    for n in node_dict.values():
        queue.append(n)

    # Count the connected components
    components = 0
    while len(queue) > 0:
        n = queue.pop()
        if n.label not in visited:
            components += 1
            search(visited, n)

    # Print the result
    print components


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    main(sys.argv[1])
