
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    # TODO
    print seqs


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
