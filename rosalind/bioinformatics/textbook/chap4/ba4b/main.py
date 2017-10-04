
import sys
from rosalind.common import util


def find_encodings(dna, protein):
    encodings = []
    # TODO
    # encodings.append("ATGGCC")
    # encodings.append("GGCCAT")
    # encodings.append("ATGGCC")
    return encodings


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        dna = fp.readline().strip()
        protein = fp.readline().strip()
    encodings = find_encodings(dna, protein)
    print encodings


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
