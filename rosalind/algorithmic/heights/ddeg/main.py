
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn


def main(fname):
    # Read in the graph
    with open(util.find_file(fname), "r") as fp:
        node_dict = debruijn.read_edge_list(fp)

    # Build a sorted list out of the nodes
    # nodes = node_dict.values().sort(key=lambda x: int(x.label))
    nodes = node_dict.values()
    nodes.sort(key=lambda x: int(x.label))

    print "Nodes:"
    print nodes

    # Go through each node and sum the degree of its neighbors
    for n in nodes:
        print n.out_edges, n.in_edges
    # TODO


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    main(sys.argv[1])
