
import sys
from rosalind.common import util


def compute_minkowski_difference(s1, s2):
    mindiff = []
    for a in s1:
        for b in s2:
            mindiff.append(a - b)
    return mindiff


def find_largest_multiplicity(s):
    scale = 100000
    counts = {}
    for i in s:
        x = round(i * scale)    # make ints
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    big = max(counts, key=lambda key: counts[key])
    num = counts[big]
    return num, big / scale


def convolve(s1, s2):
    mindiff = compute_minkowski_difference(s1, s2)
    return find_largest_multiplicity(mindiff)


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        s1 = map(float, fp.readline().split())
        s2 = map(float, fp.readline().split())
    num, big = convolve(s1, s2)
    print num
    print big


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
