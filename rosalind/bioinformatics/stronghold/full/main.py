
import sys
from rosalind.common import util
# from rosalind.bioinformatics.common import masses


def infer_peptide(parent, weights):
    # masses.get_amino_acid(186)
    # TODO
    return "KEKEP"


def main(fname):
    L = []
    with open(util.find_file(fname), "r") as fp:
        for line in fp:
            L.append(float(line))
    print infer_peptide(L[0], L[1:])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
