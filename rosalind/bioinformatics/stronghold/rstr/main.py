
import sys
from rosalind.common import util


def compute_seq_likelihood(seq, gc):
    aa_probs = {
            'G': gc / 2.0,
            'C': gc / 2.0,
            'A': (1 - gc) / 2.0,
            'T': (1 - gc) / 2.0
            }

    prob = 1
    for c in seq:
        prob *= aa_probs[c]
    return prob


def compute_probability(N, x, dna):
    seq_prob = compute_seq_likelihood(dna, x)
    prob = 1 - (1 - seq_prob) ** N
    return prob


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        bits = fp.readline().split()
        N = int(bits[0])
        x = float(bits[1])

        dna = fp.readline().strip()

    prob = compute_probability(N, x, dna)

    print round(prob, 3)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
