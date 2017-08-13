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

def print_prof(p):
    for c in ['A', 'C', 'G', 'T']:
        print c + ': ' + " ".join(map(str, p[c]))

def add_to_prof(p, s):
    for i, c in enumerate(s):
        p[c][i] += 1

def find_consensus(p):
    cons = ""
    for i in xrange(len(p['A'])):
        num = 0
        for c in ['A', 'C', 'G', 'T']:
            if p[c][i] > num:
                char = c
                num = p[c][i]
        cons += char
    return cons

# Read DNA and set up profile "matrix"
seqs = read_fasta(sys.argv[1])
m = len(seqs.values()[0]) # sequence length
prof = {
    'A': [0] * m,
    'C': [0] * m,
    'G': [0] * m,
    'T': [0] * m
}

for seq in seqs.values():
    add_to_prof(prof, seq)

print find_consensus(prof)
print_prof(prof)

