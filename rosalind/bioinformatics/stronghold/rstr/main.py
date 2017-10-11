
import sys
from rosalind.common import util


def compute_seq_likelihood(seq, gc):
    aaProbs = {
            'G': gc / 2.0,
            'C': gc / 2.0,
            'A': (1 - gc) / 2.0,
            'T': (1 - gc) / 2.0
            }

    cProb = 1
    for c in seq:
        cProb *= aaProbs[c]
    return cProb


def compute_probability(N, x, dna):
    sProb = compute_seq_likelihood(dna, x)
    print "sProb:", sProb
    print "Maybe:", sProb * N
    # TODO
    # return 0.689
    return 0


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        bits = fp.readline().split()
        N = int(bits[0])
        x = float(bits[1])

        dna = fp.readline().strip()

    prob = compute_probability(N, x, dna)

    print N, x, dna
    print prob


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
