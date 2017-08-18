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

def print_edges(seqs):
    for name1,seq1 in seqs.items():
        for name2,seq2 in seqs.items():
            if name1 != name2:
                if seq1[-3:] == seq2[:3]:
                    print name1, name2

seqs = read_fasta(sys.argv[1])
print_edges(seqs)

