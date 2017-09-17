
import sys
from rosalind.common import util


def build_graph(seq, k):
    # TODO - build the graph
    return []


def main(fname):
    with open(util.find_file(sys.argv[1]), "r") as fp:
        k = int(fp.readline())
        seq = fp.readline().strip()

    graph = build_graph(seq, k)

    print "TBD:", graph


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
