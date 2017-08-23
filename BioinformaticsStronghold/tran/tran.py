
import sys

if len(sys.argv) != 2:
    print "Please enter the name of the file to read!"
    sys.exit(1)


def read_fasta(fname):
    seqs = []
    with open(fname, "r") as ins:
        for line in ins:
            line = line.strip()
            if line[0] == '>':
                seqs.append('')
            else:
                seqs[len(seqs) - 1] += line
    return seqs


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
    seqs = read_fasta(fname)
    if len(seqs[0]) != len(seqs[1]):
        print "Sequences have different lengths!"
        sys.exit(1)
    print compute_ratio(seqs[0], seqs[1])


main(sys.argv[1])

