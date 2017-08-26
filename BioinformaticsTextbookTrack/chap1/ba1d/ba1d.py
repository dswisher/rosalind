
import sys

if len(sys.argv) < 2:
    print "You must specify the name of the file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    pat = file.readline().strip()
    seq = file.readline().strip()

def pattern_count(seq, pat):
    list = []
    for i in xrange(len(seq) - len(pat)):
        if seq[i:i + len(pat)] == pat:
            list.append(i)
    return list

print " ".join(map(str, pattern_count(seq, pat)))

