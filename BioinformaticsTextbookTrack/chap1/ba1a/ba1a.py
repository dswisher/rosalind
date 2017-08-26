
import sys

if len(sys.argv) < 2:
    print "You must specify the name of the file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    seq = file.readline().strip()
    pat = file.readline().strip()

count = 0
plen = len(pat)
for i in xrange(len(seq)):
    if seq[i:i + plen] == pat:
        count += 1

print count

