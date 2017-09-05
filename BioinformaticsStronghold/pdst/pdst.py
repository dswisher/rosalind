
import sys


def read_fasta(fname):
    seqs = []
    with open(fname, "r") as ins:
        for line in ins:
            line = line.strip()
            if line[0] == '>':
                seqs.append('')
            else:
                seqs[len(seqs) - 1] += line
    return seqs


def print_matrix(m):
    for x in xrange(len(m)):
        line = ""
        for y in xrange(len(m)):
            if len(line) > 0:
                line += " "
            line += str(m[x][y])
        print line


def compute_distance(seq1, seq2):
    tot = len(seq1)
    misses = 0
    for i in xrange(tot):
        if seq1[i] != seq2[i]:
            misses += 1
    return float(misses) / tot


def compute_matrix(seqs):
    n = len(seqs)
    mat = [[0 for x in xrange(n)] for y in xrange(n)]
    for x in xrange(n):
        for y in xrange(n):
            mat[x][y] = compute_distance(seqs[x], seqs[y])
    return mat


def main():
    if len(sys.argv) != 2:
        print "Please enter the name of the data file to load!"
        sys.exit(1)

    seqs = read_fasta(sys.argv[1])
    mat = compute_matrix(seqs)
    print_matrix(mat)


main()
