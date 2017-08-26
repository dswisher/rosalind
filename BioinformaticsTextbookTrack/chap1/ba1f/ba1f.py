
import sys

if len(sys.argv) != 2:
    print "Usage: python ba1f.py <file>"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    seq = file.readline().strip()

skew = [0] * len(seq)
for i in xrange(1, len(seq)):
    if seq[i] == 'C':
        skew[i] = skew[i-1] - 1
    elif seq[i] == 'G':
        skew[i] = skew[i-1] + 1
    else:
        skew[i] = skew[i-1]

mval = min(skew)
result = []
for i in xrange(len(skew)):
    if skew[i] == mval:
        result.append(i + 1)

print " ".join(map(str, result))

