
import sys

if len(sys.argv) != 2:
    print "Usage: python ba1f.py <file>"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    seq1 = file.readline().strip()
    seq2 = file.readline().strip()

if len(seq1) != len(seq2):
    print "Sequences have different lengths!"
    sys.exit(1)

ham = 0;
for i in xrange(0, len(seq1)):
    if seq1[i] != seq2[i]:
        ham += 1

print ham

