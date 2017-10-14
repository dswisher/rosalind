
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta


# See https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

def compute_matrix(X, Y):
    m = len(X)
    n = len(Y)
    C = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    #  return C[m,n]
    return C


def backtrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    if X[i-1] == Y[j-1]:
        return backtrack(C, X, Y, i-1, j-1) + X[i-1]
    if C[i][j-1] > C[i-1][j]:
        return backtrack(C, X, Y, i, j-1)
    return backtrack(C, X, Y, i-1, j)


def print_matrix(C):
    for x in range(len(C)):
        s = ""
        for y in range(len(C[0])):
            s += " " + str(C[x][y])
        print s


def find_longest_common_subsequence(s1, s2):
    sys.setrecursionlimit(5000)
    C = compute_matrix(s1, s2)
    # print_matrix(C)
    lcs = backtrack(C, s1, s2, len(s1), len(s2))
    return lcs


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    lcs = find_longest_common_subsequence(seqs[0], seqs[1])
    print lcs


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
