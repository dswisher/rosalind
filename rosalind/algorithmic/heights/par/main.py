
import sys
from rosalind.common import util


def swap(A, i, j):
    foo = A[i]
    A[i] = A[j]
    A[j] = foo


def partition(A, lo, hi):
    pivot = A[lo]
    i = lo - 1
    j = hi + 1
    while True:
        while True:
            i = i + 1
            if A[i] > pivot:
                break

        while True:
            j = j - 1
            if A[j] < pivot:
                break

        if i >= j:
            swap(A, 0, j)
            return j

        swap(A, i, j)


def main():
    if len(sys.argv) != 2:
        print "Please enter the name of the data file to load!"
        sys.exit(1)

    with open(util.find_file(sys.argv[1]), "r") as fp:
        fp.readline()   # skip n
        A = map(int, fp.readline().split())

    partition(A, 0, len(A) - 1)

    print " ".join(map(str, A))


main()
