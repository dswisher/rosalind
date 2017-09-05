
import sys
from biotools import enumerate_kmers


def read_data():
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    with open(sys.argv[1], "r") as fp:
        dna = fp.readline().strip()
        k = int(fp.readline())
        l = [map(float, line.split(' ')) for line in fp]
    return (k, dna, l)


def nuc_to_index(nuc):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[nuc]


def compute_prob(profile, seq):
    prob = 1
    for i in xrange(len(seq)):
        j = nuc_to_index(seq[i])
        prob *= profile[j][i]
    return prob


def find_most_probable(profile, dna, k):
    best_kmer = None
    best_prob = 0
    for kmer in enumerate_kmers(dna, k):
        p = compute_prob(profile, kmer)
        if p > best_prob:
            best_prob = p
            best_kmer = kmer
    return best_kmer


k, dna, profile = read_data()

print find_most_probable(profile, dna, k)
