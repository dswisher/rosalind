
import sys
from biotools import distance_between_pattern_and_strings, number_to_pattern


def read_input():
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    with open(sys.argv[1], "r") as fp:
        k = int(fp.readline())
        dna = [x.strip() for x in fp.readlines()]
    return (k, dna)


def find_median(dna_strings, k):
    distance = sys.maxint
    for i in xrange(0, pow(4, k)):
        pattern = number_to_pattern(i, k)
        d = distance_between_pattern_and_strings(pattern, dna_strings)
        if d < distance:
            distance = d
            median = pattern
        elif d == distance:
            print "second match at dist", d, " is", pattern
    print "min dist:", distance
    return median


def main():
    k, dna_strings = read_input()
    print find_median(dna_strings, k)


main()
