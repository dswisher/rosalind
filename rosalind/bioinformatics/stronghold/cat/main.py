
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


already_seen = {}
pairings = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}


def count_matchings(seq):
    # base case
    if len(seq) < 2:
        return 1

    # if we've already seen it, we're done
    if seq in already_seen:
        return already_seen[seq]

    # match the first item with all other pairs
    num = 0
    for i in xrange(1, len(seq), 2):
        if seq[0] == pairings[seq[i]]:
            # found a pair, compute matchings in each subset
            num += count_matchings(seq[1:i]) * count_matchings(seq[i+1:])

    # remember, so we don't have to compute again
    already_seen[seq] = num % 1000000

    # return the result
    return already_seen[seq]


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    print count_matchings(seqs[0])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
