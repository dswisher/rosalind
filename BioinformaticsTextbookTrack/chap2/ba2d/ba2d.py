
import sys
from biotools import enumerate_kmers, compute_score
from biotools import build_profile, find_most_probable, find_consensus


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
    all_kmers = build_kmers(dna, k)
    best_motifs = [item[0] for item in all_kmers]
    best_score = sys.maxint
    for kmer in all_kmers[0]:
        motifs = [kmer]
        for i in xrange(1, t):
            profile = build_profile(motifs, k)
            motif_i = find_most_probable(profile, dna[i], k)
            motifs.append(motif_i)
        consensus = find_consensus(build_profile(motifs, k), k)
        score = compute_score(consensus, motifs)
        if score < best_score:
            best_score = score
            best_motifs = motifs
    return best_motifs


def main(fname):
    k, t, dna = read_data(fname)
    motifs = greedy_motif_search(dna, k, t)
    for m in motifs:
        print m


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python ba2d.py <filename>"
        sys.exit(1)
    main(sys.argv[1])
