
import sys

if len(sys.argv) != 2:
    print "You must enter the name of the file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    pattern = file.readline().strip()
    d = int(file.readline())


def hamming_distance(seq1, seq2):
    ham = 0;
    for i in xrange(0, len(seq1)):
        if seq1[i] != seq2[i]:
            ham += 1
    return ham


def neighbors(pattern, d):
    if d == 0:
        return pattern
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


for n in neighbors(pattern, d):
    print n

