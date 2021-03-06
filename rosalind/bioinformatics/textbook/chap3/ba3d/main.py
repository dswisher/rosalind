
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn, kmers


def build_graph(seq, k):
    # TODO - can we wire the "yield" result from kmers.enum right
    #        into debruijn.create_graph?
    seqs = []
    for s in kmers.enumerate(seq, k):
        seqs.append(s)
    graph = debruijn.create_graph(seqs)
    return graph


def main(fname):
    with open(util.find_file(sys.argv[1]), "r") as fp:
        k = int(fp.readline())
        seq = fp.readline().strip()

    graph = build_graph(seq, k)

    for line in debruijn.format_graph(graph):
        print line


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
