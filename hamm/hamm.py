import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)

def read_dna(fname):
    lines = []
    with open(fname, "r") as ins:
        for line in ins:
            line = line.strip()
            lines.append(line)
    return lines[0:2]

(l1, l2) = read_dna(sys.argv[1])

if len(l1) != len(l2):
    print 'DNA strand lengths differ!'
    sys.exit(1)

diffs = 0
for i in range(0, len(l1)):
    if l1[i] != l2[i]:
        diffs += 1

print diffs

