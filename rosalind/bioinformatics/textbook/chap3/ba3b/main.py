
import sys
from rosalind.common import util


def reconstruct_string(seqs):
    seq = seqs[0]
    for s in seqs[1:]:
        seq += s[-1:]
    return seq


def main(fname):
    seqs = []
    with open(util.find_file(sys.argv[1]), "r") as fp:
        for line in fp:
            seqs.append(line.strip())
    result = reconstruct_string(seqs)
    print result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
