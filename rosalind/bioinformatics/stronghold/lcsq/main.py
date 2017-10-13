
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


# See https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
#
# function LCSLength(X[1..m], Y[1..n])
#     C = array(0..m, 0..n)
#     for i := 0..m
#        C[i,0] = 0
#     for j := 0..n
#        C[0,j] = 0
#     for i := 1..m
#         for j := 1..n
#             if X[i] = Y[j]
#                 C[i,j] := C[i-1,j-1] + 1
#             else
#                 C[i,j] := max(C[i,j-1], C[i-1,j])
#     return C[m,n]
#
# function backtrack(C[0..m,0..n], X[1..m], Y[1..n], i, j)
#     if i = 0 or j = 0
#         return ""
#     if  X[i] = Y[j]
#         return backtrack(C, X, Y, i-1, j-1) + X[i]
#     if C[i,j-1] > C[i-1,j]
#         return backtrack(C, X, Y, i, j-1)
#     return backtrack(C, X, Y, i-1, j)


def compute_matrix(X, Y):
    m = len(X)
    n = len(Y)
    C = [[0 for x in range(m)] for y in range(n)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                C[j][i] = C[j-1][i-1] + 1
            else:
                C[j][i] = max(C[j][i-1], C[j-1][i])
    #  return C[m,n]
    return C


def print_matrix(C):
    for x in range(len(C[0])):
        s = ""
        for y in range(len(C)):
            s += " " + str(C[y][x])
        print s


def find_longest_common_subsequence(s1, s2):
    C = compute_matrix(s1, s2)
    print_matrix(C)
    # TODO
    return "TODO"


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    lcs = find_longest_common_subsequence(seqs[0], seqs[1])
    print seqs
    print lcs


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
