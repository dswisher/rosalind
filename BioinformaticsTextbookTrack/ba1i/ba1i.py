
import sys


def symbol_to_number(s):
    return { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }[s]


def number_to_symbol(i):
    return { 0: 'A', 1: 'C', 2:'G', 3:'T' }[i]


def pattern_to_number(pat):
    if len(pat) == 0:
        return 0
    symbol = pat[-1:]
    prefix = pat[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefixIndex = index / 4
    r = index % 4
    symbol = number_to_symbol(r)
    prefixPattern = number_to_pattern(prefixIndex, k - 1)
    return prefixPattern + symbol


def hamming_distance(seq1, seq2):
    ham = 0;
    for i in xrange(0, len(seq1)):
        if seq1[i] != seq2[i]:
            ham += 1
    return ham


def neighbors(pattern, d):
    if len(pattern) == 0:
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
            for x in ['A', 'C', 'G', 'T']:
                neighborhood.add(x + text)
        else:
            neighborhood.add(pattern[:1] + text)
    return neighborhood


def compute_frequencies(text, k, d):
    frequency_array = [0] * pow(4, k)

    for i in xrange(0, 1 + len(text) - k):
        subj = text[i:i+k]
        neighborhood = neighbors(subj, d)
        for pattern in neighborhood:
            j = pattern_to_number(pattern)
            frequency_array[j] += 1

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

    with open(sys.argv[1], "r") as file:
        seq = file.readline().strip()
        k, d = map(int, file.readline().split())

    pats = frequent_words_with_mismatches(seq, k, d)
    print " ".join(pats)


if __name__ == "__main__":
    main()

