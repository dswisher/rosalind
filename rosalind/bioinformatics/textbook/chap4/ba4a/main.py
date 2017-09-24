
import sys
from rosalind.bioinformatics.common import seqio
from rosalind.bioinformatics.common import rna


def main(fname):
    seq = seqio.read_one(fname)
    prot = rna.translate(seq)
    print prot


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
