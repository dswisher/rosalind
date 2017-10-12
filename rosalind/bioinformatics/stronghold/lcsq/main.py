
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def find_longest_common_subsequence(s1, s2):
    # TODO
    return "TODO"


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    lcs = find_longest_common_subsequence(seqs[0], seqs[1])
    print seqs
    print lcs


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
