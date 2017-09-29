
import sys
from rosalind.common import util


def compute_probability(N, x, dna):
    # TODO
    return 0.689


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        bits = fp.readline().split()
        N = int(bits[0])
        x = float(bits[1])

        dna = fp.readline().strip()

    print N, x, dna


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
