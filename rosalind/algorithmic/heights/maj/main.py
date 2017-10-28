
import sys
from rosalind.common import util


def find_candidate(arr):
    index = 0
    count = 1
    for i in xrange(1, len(arr)):
        if arr[i] == arr[index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            index = i
            count = 1
    return arr[index]


def is_majority(arr, num):
    count = 0
    for i in xrange(len(arr)):
        if arr[i] == num:
            count += 1
    return count >= len(arr) / 2


def find_majority(arr):
    x = find_candidate(arr)
    if is_majority(arr, x):
        return x
    return -1


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        k, n = map(int, fp.readline().split())
        elems = []
        for i in xrange(k):
            arr = map(int, fp.readline().split())
            elems.append(find_majority(arr))
    print " ".join(map(str, elems))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    main(sys.argv[1])
