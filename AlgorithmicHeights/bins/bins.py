
import sys

if len(sys.argv) != 2:
    print "usage: python bins.py <filename>"
    sys.exit(1)

with open(sys.argv[1], "r") as fp:
    fp.readline()
    fp.readline()
    A = map(int, fp.readline().split())
    B = map(int, fp.readline().split())


def binary_search(A, x):
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = (l + r) / 2

        if A[mid] == x:
            return mid + 1

        if A[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1


nums = []
for i in B:
    nums.append(binary_search(A, i))
print " ".join(map(str, nums))
