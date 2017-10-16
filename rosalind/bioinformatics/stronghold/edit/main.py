
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


def edit_distance(s, t):
    # See https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
    # For all i and j, d[i,j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t.
    # Note that d has (m+1) x (n+1) values.

    m = len(s)
    n = len(t)

    # let d be a 2-d array of int with dimensions [0..m, 0..n]
    d = [[0 for x in range(n+1)] for y in range(m+1)]

    #    for i in [0..m]
    #      d[i, 0] <- i // the distance of any first string to an empty second string
    #                  // (transforming the string of the first i characters of s into
    #                  // the empty string requires i deletions)
    #    for j in [0..n]
    #      d[0, j] <- j // the distance of any second string to an empty first string
    #
    #    for j in [1..n]
    #      for i in [1..m]
    #        if s[i] = t[j] then
    #          d[i, j] <- d[i-1, j-1]        // no operation required
    #        else
    #          d[i, j] <- minimum of
    #                     (
    #                       d[i-1, j] + 1,  // a deletion
    #                       d[i, j-1] + 1,  // an insertion
    #                       d[i-1, j-1] + 1 // a substitution
    #                     )

    return d[m][n]


def find_edit_distance(s, t):
    # The algo on wikipedia uses 1-based indexing for the string.
    # Shift things to make that true here...
    return edit_distance(" " + s, " " + t)


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    ed = find_edit_distance(seqs[0], seqs[1])
    print ed


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
