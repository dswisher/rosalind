
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn


def build_graph(seqs):
    graph = debruijn.create_graph(seqs)
    return graph


def format_graph(graph):
    for n in graph.values():
        l = n.label
        r = []
        for e in n.out_edges:
            r.append(e.tail.label)
        if len(r) > 0:
            yield l + " -> " + ",".join(sorted(r))


def main(fname):
    with open(util.find_file(sys.argv[1]), "r") as fp:
        seqs = fp.read().splitlines()

    graph = build_graph(seqs)

    for line in format_graph(graph):
        print line


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
