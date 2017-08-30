
import sys

def parse_set(n, s):
    nums = map(int, s[1:-1].split(","))
    ss = [0] * n
    for i in nums:
        ss[i - 1] = 1
    return ss


def print_set(A):
    s = "{"
    for i in xrange(len(A)):
        if A[i] == 1:
            if len(s) > 1: s += ", "
            s += str(i + 1)
    s += "}"
    print s


def read_input(fname):
    with open(fname, "r") as fp:
        n = int(fp.readline())
        A = parse_set(n, fp.readline().strip())
        B = parse_set(n, fp.readline().strip())
        
    return (n, A, B)

# TODO - rewrite these in terms of a lambda

def union(A, B):
    C = [0] * len(A)
    for i in xrange(len(A)):
        if A[i] == 1 or B[i] == 1:
            C[i] = 1
    return C


def intersection(A, B):
    C = [0] * len(A)
    for i in xrange(len(A)):
        if A[i] == 1 and B[i] == 1:
            C[i] = 1
    return C


def minus(A, B):
    C = [0] * len(A)
    for i in xrange(len(A)):
        if A[i] == 1 and B[i] == 0:
            C[i] = 1
    return C


def complement(A):
    C = [0] * len(A)
    for i in xrange(len(A)):
        if A[i] == 0:
            C[i] = 1
    return C


def main():
    if len(sys.argv) != 2:
        print "Please enter the name of the data file to read."
        sys.exit(1)

    n, A, B = read_input(sys.argv[1])

    print_set(union(A, B))
    print_set(intersection(A, B))
    print_set(minus(A, B))
    print_set(minus(B, A))
    print_set(complement(A))
    print_set(complement(B))


main()

