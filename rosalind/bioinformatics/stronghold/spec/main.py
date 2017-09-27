
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import masses


def infer_protein(weights):
    protein = ""
    last = weights[0]
    for i in xrange(1, len(weights)):
        protein += masses.get_amino_acid(weights[i] - last)
        last = weights[i]
    return protein


def main(fname):
    weights = []
    with open(util.find_file(fname), "r") as fp:
        for line in fp:
            weights.append(float(line))
    protein = infer_protein(weights)
    print protein


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
