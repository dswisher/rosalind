
import sys
from rosalind.bioinformatics.common import seqio


def assemble_circular_chromosome(seqs):
    # TODO
    return "GATTACA"


def main(fname):
    seqs = seqio.read_list(fname, __file__)
    chromosome = assemble_circular_chromosome(seqs)
    print seqs
    print chromosome


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
