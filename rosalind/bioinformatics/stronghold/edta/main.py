
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def print_matrix(d, m, n):
    for y in range(n+1):
        s = ""
        for x in range(m+1):
            s += " " + str(d[x][y])
        print s


def edit_distance(s, t):
    # See https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
    # For all i and j, d[i,j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t.
    # Note that d has (m+1) x (n+1) values.

    m = len(s) - 1
    n = len(t) - 1

    # let d be a 2-d array of int with dimensions [0..m, 0..n]
    d = [[0 for x in range(n+1)] for y in range(m+1)]

    # let bt be a matrix that keeps track of how we got to each cell
    # in d: "eql", "ins", "del" or "sub" (inefficient, but easy to debug)
    ops = ["ins", "del", "sub"]
    bt = [[" x " for x in range(n+1)] for y in range(m+1)]

    # The distance of any first string to an empty second string
    # (need to do i deletions)
    for i in xrange(m+1):
        d[i][0] = i

    # The distance of any second string to an empty first string
    for j in xrange(n+1):
        d[0][j] = j

    for j in xrange(1, n+1):
        for i in xrange(1, m+1):
            if s[i] == t[j]:
                # Strings are equal at this position; no edit required
                d[i][j] = d[i-1][j-1]
                bt[i][j] = "eql"
            else:
                deld = d[i-1][j] + 1    # deletion cost
                insd = d[i][j-1] + 1    # insert cost
                subd = d[i-1][j-1] + 1  # substitution cost
                dist = (insd, deld, subd)
                d[i][j] = min(dist)
                bt[i][j] = ops[dist.index(d[i][j])]

    print_matrix(d, m, n)
    print_matrix(bt, m, n)

    return (d[m][n], bt)


def align(bt, s, t):
    # TODO
    return ("=" + s + "=", "+" + t + "+")


def edit_distance_alignment(s, t):
    dist, bt = edit_distance(s, t)
    os, ot = align(bt, s, t)
    return (dist, os, ot)


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    align, os, ot = edit_distance_alignment(seqs[0], seqs[1])
    print align
    print os
    print ot


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
