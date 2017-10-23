
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def find_corrections(seqs):
    # TODO
    return ["TBD"]
    # return ["TTCAT->TTGAT", "GAGGA->GATGA", "TTTCC->TTTCA"]


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    corrections = find_corrections(seqs)
    print corrections


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
