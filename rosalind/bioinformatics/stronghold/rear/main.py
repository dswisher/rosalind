
import sys
from rosalind.common import util


# Calculate b(p)
def num_breakpoints(p):
    last = p[0]
    num = 0
    for i in xrange(1, len(p)):
        if abs(p[i] - last) != 1:
            num += 1
        last = p[i]
    return num


# Find decreasing strips in p and return them as a tuple of (start-pos, end-pos)
def find_strips(p):
    strips = []
    # TODO
    return strips


def reversal_distance(a, b):
    print "p=a, ", a, " -> bp(p)=", num_breakpoints(a), ", strips: ", find_strips(a)
    # TODO
    return 0


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        distances = []
        while True:
            a = map(int, fp.readline().split())
            b = map(int, fp.readline().split())
            distances.append(reversal_distance(a, b))
            if fp.readline() == '':
                break
    print " ".join(map(str, distances))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
