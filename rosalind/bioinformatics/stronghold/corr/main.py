
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta
from rosalind.bioinformatics.common import kmers


def build_counts(seqs):
    comps = dict()
    for s in seqs:
        if s in comps:
            comps[s] += 1
        else:
            comps[s] = 1
        comp = kmers.reverse_complement(s)
        if comp in comps:
            comps[comp] += 1
        else:
            comps[comp] = 2
    return comps


def find_corrections(seqs):
    corrs = []
    comps = build_counts(seqs)
    # print comps
    for s1, num in comps.iteritems():
        if num == 1:
            for s2 in comps:
                if kmers.hamming_distance(s1, s2) == 1:
                    corrs.append(s1 + "->" + s2)
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
