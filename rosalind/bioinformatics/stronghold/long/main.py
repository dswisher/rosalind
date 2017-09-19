
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def max_overlap(s1, s2):
    mlap = 0
    for k in xrange(1, min(len(s1), len(s2))):
        if s1[-k:] == s2[:k]:
            mlap = k
    return mlap


def find_max_overlap(seqs, pos):
    max_olap = 0
    max_i = -1
    for i in xrange(len(seqs)):
        if i != pos:
            olap = max_overlap(seqs[pos], seqs[i])
            if olap > max_olap:
                max_olap = olap
                max_i = i
    return max_i


def find_shortest_superstring(seqs):
    pos = 0
    bail = 0    # Temporary infinite loop prevention
    while len(seqs) > 1 and bail < 20:
        olap = find_max_overlap(seqs, pos)
        print pos, olap
        bail += 1
    # TODO
    # return "ATTAGACCTGCCGGAATAC"
    return "FRED"


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    print (find_shortest_superstring(seqs))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
