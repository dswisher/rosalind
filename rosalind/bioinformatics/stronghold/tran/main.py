
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def compute_ratio(seq1, seq2):
    transitions = set(['AG', 'GA', 'CT', 'TC'])
    transversions = set(['AC', 'CA', 'GT', 'TG', 'AT', 'TA', 'CG', 'GC'])
    numTransitions = 0
    numTransversions = 0
    for i in xrange(len(seq1)):
        x = seq1[i] + seq2[i]
        if x in transitions:
            numTransitions += 1
        elif x in transversions:
            numTransversions += 1
    return float(numTransitions) / numTransversions


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    if len(seqs[0]) != len(seqs[1]):
        print "Sequences have different lengths!"
        sys.exit(1)
    print compute_ratio(seqs[0], seqs[1])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
