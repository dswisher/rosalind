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

(s, t) = read_dna(sys.argv[1])

found = []
pos = 0
beg = 0

while pos != -1:
    pos = s.find(t, beg)
    if pos != -1:
        found.append(pos + 1)
        beg = pos + 1

print " ".join(map(str, found))

