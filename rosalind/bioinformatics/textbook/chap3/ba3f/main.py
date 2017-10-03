
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn
from rosalind.bioinformatics.common import eulerian


def main(fname):
    with open(util.find_file(sys.argv[1]), "r") as fp:
        graph = debruijn.read_adjacency_list(fp)

    path = eulerian.find_cycle(graph)
    print eulerian.format_path(path)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
