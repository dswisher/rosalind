
import sys
from rosalind.common import util


def get_amino_acid(weight):
    weights = {"A":  71.03711, "C": 103.00919, "D": 115.02694,
               "E": 129.04259, "F": 147.06841, "G":  57.02146,
               "H": 137.05891, "I": 113.08406, "K": 128.09496,
               "L": 113.08406, "M": 131.04049, "N": 114.04293,
               "P":  97.05276, "Q": 128.05858, "R": 156.10111,
               "S":  87.03203, "T": 101.04768, "V":  99.06841,
               "W": 186.07931, "Y": 163.06333}
    diff = 1e6
    best = None
    for aa, w in weights.iteritems():
        d = abs(weight - w)
        if d < diff:
            diff = d
            best = aa
    return best


def infer_protein(weights):
    protein = ""
    last = weights[0]
    for i in xrange(1, len(weights)):
        protein += get_amino_acid(weights[i] - last)
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
