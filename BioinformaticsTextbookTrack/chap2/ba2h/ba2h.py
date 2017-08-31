
import sys
from biotools import distance_between_pattern_and_strings


def read_input():
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    with open(sys.argv[1], "r") as fp:
        pattern = fp.readline().strip()
        dna = fp.readline().strip().split(" ")
    return (pattern, dna)


def main():
    pat, dna = read_input()
    dist = distance_between_pattern_and_strings(pat, dna)
    print dist


main()
