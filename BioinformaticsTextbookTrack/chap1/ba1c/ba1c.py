
import sys

if len(sys.argv) < 2:
    print "You must specify the name of the file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    seq = file.readline().strip()

def complement(base):
    return { "A": "T", "T": "A", "G": "C", "C": "G" }[base]

def complement_seq(seq):
    comp = ""
    for c in seq:
        comp += complement(c)
    return comp[::-1]

def pattern_count(seq, pat):
    count = 0
    plen = len(pat)
    for i in xrange(len(seq) - plen):
        if seq[i:i + plen] == pat:
            count += 1
    return count

def frequent_words(seq, k):
    freq = set()
    count = []
    for i in xrange(len(seq) - k):
        pat = seq[i:i+k]
        count.append(pattern_count(seq, pat))
    max_count = max(count)
    for i in xrange(len(seq) - k):
        if count[i] == max_count:
            freq.add(seq[i:i+k])
    return sorted(freq)

print complement_seq(seq)

