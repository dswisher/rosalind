
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn


def neighbor_degree(node):
    sum = 0
    for e in node.out_edges:
        sum += e.tail.degree()
    for e in node.in_edges:
        sum += e.head.degree()
    return sum


def main(fname):
    # Read in the graph
    with open(util.find_file(fname), "r") as fp:
        node_dict = debruijn.read_edge_list(fp)

    # Build a sorted list out of the nodes
    nodes = node_dict.values()
    nodes.sort(key=lambda x: int(x.label))

    # Go through each node and sum the degree of its neighbors
    counts = []
    for n in nodes:
        counts.append(neighbor_degree(n))

    # Print the result
    print " ".join(map(str, counts))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    main(sys.argv[1])
