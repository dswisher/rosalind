
import sys
from rosalind.bioinformatics.common import seqio
from rosalind.bioinformatics.common import debruijn
from rosalind.bioinformatics.common import eulerian


def assemble_circular_chromosome(seqs):
    graph = debruijn.create_graph(seqs)
    path = eulerian.find_cycle(graph)
    str = ""
    for n in path:
        str += n.label[0]
    return str[:-1]


def main(fname):
    seqs = seqio.read_list(fname, __file__)
    chromosome = assemble_circular_chromosome(seqs)
    print chromosome


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
