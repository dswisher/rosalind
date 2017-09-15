
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta
from rosalind.bioinformatics.common import kmers


def count_kmers(seq, k):
    # TODO - use yield?
    result = []
    for kmer in kmers.list(k):
        index = 0
        num = 0
        while index < len(seq):
            index = seq.find(kmer, index)
            if index == -1:
                break
            num += 1
            index += 1  # want overlaps
        result.append(num)
    return result


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    result = count_kmers(seqs[0], 4)
    print " ".join(map(str, result))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
