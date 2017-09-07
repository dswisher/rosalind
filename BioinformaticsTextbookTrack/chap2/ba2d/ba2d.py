
import sys
from biotools import enumerate_kmers


def read_data(fname):
    dna = []
    with open(fname, "r") as fp:
        k, t = map(int, fp.readline().split())
        for line in fp:
            dna.append(line.strip())
    return (k, t, dna)


# Build a list of lists of k-mers (one per string in dna)
def build_kmers(dna, k):
    kmers = []
    for s in dna:
        l = []
        kmers.append(l)
        for mer in enumerate_kmers(s, k):
            l.append(mer)
    return kmers


def greedy_motif_search(dna, k, t):
    kmers = build_kmers(dna, k)
    best_motifs = [item[0] for item in kmers]
    return best_motifs


def main():
    k, t, dna = read_data(sys.argv[1])
    print greedy_motif_search(dna, k, t)


main()
