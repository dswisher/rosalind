
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def edit_distance_alignment(s, t):
    # TODO
    # return (4, "PRETTY--", "PR-TTEIN")
    return ()


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    align = edit_distance_alignment(seqs[0], seqs[1])
    print align


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
