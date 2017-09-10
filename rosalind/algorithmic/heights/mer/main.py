
import sys
from rosalind.common import util

if len(sys.argv) != 2:
    print "Please enter the name of the data file!"
    sys.exit(1)

with open(util.find_file(sys.argv[1]), "r") as fp:
    n = int(fp.readline())
    A = map(int, fp.readline().split())
    m = int(fp.readline())
    B = map(int, fp.readline().split())


def merge(a, b):
    i = 0
    j = 0
    k = 0
    result = [0] * (len(a) + len(b))
    while i < len(a) or j < len(b):
        if i < len(a):
            if j < len(b):
                if a[i] < b[j]:
                    result[k] = a[i]
                    i += 1
                else:
                    result[k] = b[j]
                    j += 1
            else:
                result[k] = a[i]
                i += 1
        else:
            result[k] = b[j]
            j += 1
        k += 1
    return result


x = map(str, merge(A, B))
print " ".join(x)
