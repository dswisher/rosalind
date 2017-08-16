import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)

def read_fasta(fname):
    key = ""
    seqs = {}
    with open(fname, "r") as ins:
        for line in ins:
            line = line.strip()
            if line[0] == '>':
                key = line[1:]
                seqs[key] = ''
            else:
                seqs[key] += line
    return seqs

def compute_gc(seq):
    tot = 0
    gc = 0
    for c in seq:
        tot += 1
        if c == 'C' or c == 'G':
            gc += 1
    return 100.0 * gc / tot


seqs = read_fasta(sys.argv[1])
maxgc = 0
maxname = ''
for name,seq in seqs.items():
    gc = compute_gc(seq)
    if gc > maxgc:
        maxgc = gc
        maxname = name

print maxname
print "%.5f" % maxgc

