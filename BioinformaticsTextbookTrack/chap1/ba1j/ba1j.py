import sys


def rev_comp(seq):
    comp = { 'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    sc = ''
    for c in reversed(seq):
        if c in comp:
            sc += comp[c]
    return sc


def symbol_to_number(sym):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[sym]


def number_to_symbol(num):
    return {0: 'A', 1: 'C', 2:'G', 3:'T'}[num]


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
    ham = 0
    for i in xrange(0, len(seq1)):
        if seq1[i] != seq2[i]:
            ham += 1
    return ham


def neighbors(pattern, d):
    if not pattern:
        print "-> pattern has zero length!"
        sys.exit(1)
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


def count_patterns(freqs, subj, d):
    neighborhood = neighbors(subj, d)
    for pattern in neighborhood:
        i = pattern_to_number(pattern)
        freqs[i] += 1


def compute_frequencies(text, k, d):
    frequency_array = [0] * pow(4, k)

    for i in xrange(0, 1 + len(text) - k):
        subj = text[i:i+k]
        count_patterns(frequency_array, subj, d)
        count_patterns(frequency_array, rev_comp(subj), d)

    return frequency_array


def frequent_words_with_mismatches(text, k, d):
    patterns = []
    freqs = compute_frequencies(text, k, d)
    max_count = max(freqs)

    for i in xrange(len(freqs)):
        if freqs[i] == max_count:
            p = number_to_pattern(i, k)
            patterns.append(p)

    return patterns


def main():
    if len(sys.argv) != 2:
        print "You must enter the name of the file to load!"
        sys.exit(1)

    with open(sys.argv[1], "r") as infile:
        seq = infile.readline().strip()
        k, d = map(int, infile.readline().split())

    pats = frequent_words_with_mismatches(seq, k, d)
    print " ".join(pats)


if __name__ == "__main__":
    main()
