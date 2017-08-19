
import sys

if len(sys.argv) < 3:
    print "Usage: python pper.py n k"
    sys.exit(1)

n = int(sys.argv[1])
k = int(sys.argv[2])

prod = 1
for i in xrange(k):
    prod = (prod * (n - i)) % 1000000

print prod
