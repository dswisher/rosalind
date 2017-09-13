
import sys
from rosalind.common import util


def read_input(fname):
    seqs = []
    seq = ""
    with open(util.find_file(fname), "r") as fp:
        for line in fp:
            line = line.strip()
            if line[:1] == '>':
                if len(seq) > 0:
                    seqs.append(seq)
                seq = ""
            else:
                seq += line
        if len(seq) > 0:
            seqs.append(seq)
    return seqs


# https://stackoverflow.com/a/2894073/282725
def longest_common_substring(seqs):
    # TODO - reimplement using suffix tree
    #      https://en.wikipedia.org/wiki/Longest_common_substring_problem#Suffix_tree
    substr = ''
    if len(seqs) > 1 and len(seqs[0]) > 0:
        for i in range(len(seqs[0])):
            for j in range(len(seqs[0])-i+1):
                if j > len(substr) and all(seqs[0][i:i+j] in x for x in seqs):
                    substr = seqs[0][i:i+j]
    return substr


def main(fname):
    seqs = read_input(fname)
    print longest_common_substring(seqs)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
