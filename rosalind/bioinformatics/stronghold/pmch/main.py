
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta
import math


def calc_matches(seq):
    a = 0
    c = 0
    for s in seq:
        if s == 'A':
            a += 1
        elif s == 'C':
            c += 1
    return math.factorial(a) * math.factorial(c)


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    print calc_matches(seqs[0])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
