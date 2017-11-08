
import sys
from rosalind.common import util


def reversal_distance(a, b):
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
