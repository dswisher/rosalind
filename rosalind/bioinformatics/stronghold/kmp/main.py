
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def build_table(pattern):
    lsp = [-1] * len(pattern)
    lsp[0] = 0
    for i in xrange(1, len(pattern)):
        j = lsp[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = lsp[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lsp[i] = j
    return lsp


def main(fname):
    seq, _ = fasta.read(util.find_file(fname))
    T = build_table(seq[0])
    print " ".join(map(str, T))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
