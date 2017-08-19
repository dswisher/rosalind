
import sys

if len(sys.argv) != 7:
    print "Usage: python iev.py a b c d e f"
    sys.exit(1)

probs = [
        1.0,    # AA + AA
        1.0,    # AA + Aa
        1.0,    # AA + aa
        0.75,   # Aa + Aa
        0.5,    # Aa + aa
        0       # aa + aa
        ]

num = 0
for i in xrange(1, len(sys.argv)):
    num += float(sys.argv[i]) * probs[i - 1]

print 2 * num

