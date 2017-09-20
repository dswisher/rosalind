
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn


def main(fname):
    with open(util.find_file(sys.argv[1]), "r") as fp:
        graph = debruijn.read_adjacency_list(fp)

    # TODO - for now, just dump the graph
    for line in debruijn.format_graph(graph):
        print line


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
