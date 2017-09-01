
import sys

if len(sys.argv) != 2:
    print "Please enter the name of the data file!"
    sys.exit(1)

with open(sys.argv[1], "r") as fp:
    n = int(fp.readline())
    A = map(int, fp.readline().split())


def insertion_sort(A):
    swaps = 0
    for i in xrange(1, len(A)):
        k = i
        while k > 0 and A[k] < A[k-1]:
            x = A[k]
            A[k] = A[k-1]
            A[k-1] = x
            swaps += 1
            k = k - 1
    return swaps


swaps = insertion_sort(A)
print swaps
