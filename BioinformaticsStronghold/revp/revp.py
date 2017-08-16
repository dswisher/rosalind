import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)


def read_fasta(fname):
    seq = ""
    with open(fname, "r") as file:
        for line in file:
            line = line.strip()
            if line[0] != '>':
                seq += line
    return seq


def rev_comp(seq):
    comp = { 'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    sc = ''
    for c in reversed(seq):
        if c in comp:
            sc += comp[c]
    return sc


def main():
    seq = read_fasta(sys.argv[1])
    for i in xrange(len(seq)-3):
        for j in xrange(min(12, len(seq)-i), 3, -1):
            s = seq[i:i+j]
            if s == rev_comp(s):
                print "%d %d" % (i + 1, j)

main()

