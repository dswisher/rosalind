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

def cons(strings):
    from collections import Counter
    counters = map(Counter, zip(*strings))
    consensus = "".join(c.most_common(1)[0][0] for c in counters)
    return (counters, consensus)

def print_prof(counters):
    print "\n".join(b + ": " + " ".join(str(c[b]) for c in counters) for b in "ACGT")

seqs = read_fasta(sys.argv[1])
mat,con = cons(seqs.values())

print con
print_prof(mat)

# print mat

