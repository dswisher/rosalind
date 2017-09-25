
import sys
import math
from rosalind.common import util


def longest_decreasing_subsequence(N, X):
    # TODO - come up with a more efficient method?
    backwards = list(reversed(X))
    inc = longest_increasing_subsequence(N, backwards)
    dec = list(reversed(inc))
    return dec


def longest_increasing_subsequence(N, X):
    # noqa - see https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms
    P = [0] * N
    M = [0] * (N + 1)
    L = 0
    for i in xrange(N):
        # Binary search for largest positive j <= L such that X[M[j]] < X[i]
        lo = 1
        hi = L
        while lo <= hi:
            mid = int(math.ceil((lo + hi) / 2))
            if X[M[mid]] < X[i]:
                lo = mid+1
            else:
                hi = mid-1

        # After searching, lo is 1 greater than the
        # length of the longest prefix of X[i]
        newL = lo

        # The predecessor of X[i] is the last index of
        # the subsequence of length newL-1
        P[i] = M[newL - 1]
        M[newL] = i

        if newL > L:
            # If we found a subsequence longer than any we've
            # found yet, update L
            L = newL

    # Reconstruct the longest increasing subsequence
    S = [0] * L
    k = M[L]
    for i in xrange(L-1, -1, -1):
        S[i] = X[k]
        k = P[k]

    return S


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        n = int(fp.readline())
        pi = map(int, fp.readline().split())
    liss = longest_increasing_subsequence(n, pi)
    ldss = longest_decreasing_subsequence(n, pi)
    print " ".join(map(str, liss))
    print " ".join(map(str, ldss))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
