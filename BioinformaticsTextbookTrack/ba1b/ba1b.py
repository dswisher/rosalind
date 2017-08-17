
import sys

if len(sys.argv) < 2:
    print "You must specify the name of the file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    seq = file.readline().strip()
    k = int(file.readline().strip())

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

print " ".join(frequent_words(seq, k))

