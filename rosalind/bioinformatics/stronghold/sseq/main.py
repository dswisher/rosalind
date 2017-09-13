
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def find_subseqs(s, t):
    si = 0
    ti = 0
    pos = []
    while si < len(s) and ti < len(t):
        if s[si] == t[ti]:
            pos.append(si + 1)
            ti += 1
        si += 1
    return pos


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    pos = find_subseqs(seqs[0], seqs[1])
    print " ".join(map(str, pos))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
