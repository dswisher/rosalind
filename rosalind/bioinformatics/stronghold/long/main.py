
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


# https://stackoverflow.com/a/2894073/282725
def find_shortest_superstring(seqs):
    # TODO
    return "FRED"


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    print (seqs)
    print (find_shortest_superstring(seqs))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
