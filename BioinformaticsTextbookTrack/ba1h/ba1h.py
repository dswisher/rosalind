
import sys

if len(sys.argv) != 2:
    print "Usage: python ba1h.py <file>"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    pat = file.readline().strip()
    seq = file.readline().strip()
    d = int(file.readline())

def hamming(seq1, seq2):
    ham = 0;
    for i in xrange(0, len(seq1)):
        if seq1[i] != seq2[i]:
            ham += 1
    return ham

pos = []
for i in xrange(1 + len(seq) - len(pat)):
    can = seq[i:i+len(pat)]
    if hamming(can, pat) <= d:
        pos.append(i)

print " ".join(map(str, pos))

