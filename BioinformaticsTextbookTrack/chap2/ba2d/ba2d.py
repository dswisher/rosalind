
import sys
from biotools import enumerate_kmers, hamming_distance


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


def nuc_to_index(nuc):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[nuc]


def index_to_nuc(idx):
    return {0: 'A', 1: 'C', 2: 'G', 3: 'T'}[idx]


def build_profile(seqs, k):
    profile = [[0. for i in xrange(k)] for j in xrange(4)]
    n = len(seqs)
    delta = 1.0 / n
    for i in xrange(n):
        for j in xrange(k):
            idx = nuc_to_index(seqs[i][j])
            profile[idx][j] += delta
    return profile


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
        if (p > best_prob) or best_kmer is None:
            best_prob = p
            best_kmer = kmer
    return best_kmer


def find_consensus(profile, k):
    con = ""
    for i in xrange(k):
        m = 0
        c = 'A'
        for j in xrange(4):
            if profile[j][i] > m:
                m = profile[j][i]
                c = index_to_nuc(j)
        con += c
    return con


def compute_score(consensus, motifs):
    score = 0
    for seq in motifs:
        score += hamming_distance(consensus, seq)
    return score


def greedy_motif_search(dna, k, t):
    all_kmers = build_kmers(dna, k)
    best_motifs = [item[0] for item in all_kmers]
    best_score = sys.maxint
    for kmer in all_kmers[0]:
        motifs = [kmer]
        for i in xrange(2, t):
            profile = build_profile(motifs, k)
            motif_i = find_most_probable(profile, dna[i], k)
            motifs.append(motif_i)
        consensus = find_consensus(build_profile(motifs, k), k)
        score = compute_score(consensus, motifs)
        if score < best_score:
            best_score = score
            best_motifs = motifs
    return best_motifs


def print_profile(profile, k):
    for j in xrange(4):
        line = index_to_nuc(j) + ": "
        for i in xrange(k):
            # line += " " + str(round(profile[j][i], 2))
            line += '{:<04}'.format(profile[j][i]) + "  "
        print line


def test1():
    k = 12
    profile = build_profile(["TCGGGGGTTTTT", "CCGGTGACTTAC", "ACGGGGATTTTC",
                             "TTGGGGACTTTT", "AAGGGGACTTCC", "TTGGGGACTTCC",
                             "TCGGGGATTCAT", "TCGGGGATTCCT", "TAGGGGAACTAC",
                             "TCGGGTATAACC"], k)
    print_profile(profile, k)
    print find_consensus(profile, k)


def main(fname):
    k, t, dna = read_data(fname)
    print greedy_motif_search(dna, k, t)

    # test1()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python ba2d.py <filename>"
        sys.exit(1)
    main(sys.argv[1])
