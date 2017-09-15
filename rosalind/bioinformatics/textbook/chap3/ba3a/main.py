
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import kmers


def generate_kmers(seq, k):
    result = []
    for k in sorted(kmers.enumerate(seq, k)):
        result.append(k)
    return result


def main(fname):
    with open(util.find_file(sys.argv[1]), "r") as fp:
        k = int(fp.readline())
        seq = fp.readline().strip()

    for k in sorted(generate_kmers(seq, k)):
        print k


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
