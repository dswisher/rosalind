
import sys
from rosalind.common import util


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        # n nodes, m edges
        n, m = map(int, fp.readline().split())

        # Rest of the lines are edges
        for line in fp.readlines():
            a, b = map(int, line.split())
            print str(a) + " -> " + str(b)
            # TODO


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    main(sys.argv[1])
