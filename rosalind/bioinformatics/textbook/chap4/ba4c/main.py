
import sys
from rosalind.bioinformatics.common import seqio


def generate_spectrum(protein):
    # TODO
    # return [0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484]
    return []


def main(fname):
    protein = seqio.read_one(fname)
    spec = generate_spectrum(protein)
    print " ".join(map(str, spec))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
