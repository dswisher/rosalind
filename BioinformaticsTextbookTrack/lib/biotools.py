import sys


def rev_comp(seq):
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    sc = ''
    for c in reversed(seq):
        if c in comp:
            sc += comp[c]
    return sc


def symbol_to_number(sym):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[sym]


def number_to_symbol(num):
    return {0: 'A', 1: 'C', 2: 'G', 3: 'T'}[num]


def pattern_to_number(pat):
    if not pat:
        return 0
    symbol = pat[-1:]
    prefix = pat[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = index / 4
    remainder = index % 4
    symbol = number_to_symbol(remainder)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol


def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("patterns must be the same length")
    ham = 0
    for i in xrange(0, len(seq1)):
        if seq1[i] != seq2[i]:
            ham += 1
    return ham


def enumerate_kmers(seq, k):
    for i in xrange(0, 1 + len(seq) - k):
        subj = seq[i:i+k]
        yield subj


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


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for text in dna:
        hamming_dist = sys.maxint
        for patternp in enumerate_kmers(text, k):
            hd = hamming_distance(pattern, patternp)
            if hd < hamming_dist:
                hamming_dist = hd
        distance += hamming_dist
    return distance
