
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta
from rosalind.bioinformatics.common import kmers


def count_kmers(seq, k):
    # Build a list of all the kmers
    print seq
    for k in kmers.list(k):
        # Count the number of times k appears in seq
        print k
    # TODO - HACK
    return [4, 1, 4, 3]


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    result = count_kmers(seqs[0], 4)
    print " ".join(map(str, result))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
