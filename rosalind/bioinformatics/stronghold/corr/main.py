
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta
from rosalind.bioinformatics.common import kmers


def build_counts(seqs):
    counts = dict()
    for s in seqs:
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    for s in seqs:
        comp = kmers.reverse_complement(s)
        if comp in counts:
            counts[s] += 1
    return counts


def find_corrections(seqs):
    corrs = []
    counts = build_counts(seqs)
    print counts
    for s1 in seqs:
        num = counts[s1]
        if num == 1:
            found = False
            for s2 in seqs:
                if kmers.hamming_distance(s1, s2) == 1:
                    corrs.append(s1 + "->" + s2)
                    found = True
                    break

            if not found:
                c1 = kmers.reverse_complement(s1)
                for s2 in seqs:
                    if kmers.hamming_distance(c1, s2) == 1:
                        corrs.append(s1 + "->" + s2)
                        break
    return corrs

    for s1, num in counts.iteritems():
        if num == 1:
            found = False
            for s2 in seqs:
                if kmers.hamming_distance(s1, s2) == 1:
                    corrs.append(s1 + "->" + s2)
                    found = True
                    break
            if not found:
                c1 = kmers.reverse_complement(s1)
                for s2 in seqs:
                    if kmers.hamming_distance(c1, s2) == 1:
                        corrs.append(s1 + "->" + s2)
                        break
    return corrs


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    corrections = find_corrections(seqs)
    for c in corrections:
        print c


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
