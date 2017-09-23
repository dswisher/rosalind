
import sys
from rosalind.bioinformatics.common import seqio
from rosalind.bioinformatics.common import kmers
from rosalind.bioinformatics.common import debruijn


def make_graph(seqs):
    unique = set()
    for s in seqs:
        unique.add(s)
        unique.add(kmers.reverse_complement(s))
    graph = debruijn.create_graph(list(unique))
    return graph


def main(fname):
    seqs = seqio.read_list(fname)
    graph = make_graph(seqs)
    for line in debruijn.format_adjacency(graph):
        print line


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
