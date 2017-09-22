
import itertools


def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("patterns must be the same length")
    ham = 0
    for i in xrange(0, len(seq1)):
        if seq1[i] != seq2[i]:
            ham += 1
    return ham


def neighbors(pattern, d):
    if not pattern:
        raise ValueError("pattern cannot be zero length")
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for char in ['A', 'C', 'G', 'T']:
                neighborhood.add(char + text)
        else:
            neighborhood.add(pattern[:1] + text)
    return neighborhood


def enumerate(seq, k):
    for i in xrange(0, 1 + len(seq) - k):
        subj = seq[i:i+k]
        yield subj


def nuc_to_index(nuc):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[nuc]


def index_to_nuc(idx):
    return {0: 'A', 1: 'C', 2: 'G', 3: 'T'}[idx]


def build_profile(seqs, k, seed=0.):
    n = len(seqs)
    delta = 1.0 / n
    profile = [[seed for i in xrange(k)] for j in xrange(4)]
    for i in xrange(n):
        for j in xrange(k):
            idx = nuc_to_index(seqs[i][j])
            profile[idx][j] += delta
    return profile


def print_profile(profile, k):
    for j in xrange(4):
        line = index_to_nuc(j) + ": "
        for i in xrange(k):
            # line += " " + str(round(profile[j][i], 2))
            line += '{:<04}'.format(profile[j][i]) + "  "
        print line


def compute_prob(profile, seq):
    prob = 1
    for i in xrange(len(seq)):
        j = nuc_to_index(seq[i])
        prob *= profile[j][i]
    return prob


def find_most_probable(profile, dna, k):
    best_kmer = None
    best_prob = 0
    for kmer in enumerate(dna, k):
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


def list(k, alphabet="ACGT"):
    for tup in itertools.product(alphabet, repeat=k):
        yield ''.join(tup)
