
import sys


def read_input():
    if len(sys.argv) != 2:
        print "usage: python lcsm.py <filename>"
        sys.exit(1)
    seqs = []
    seq = ""
    with open(sys.argv[1], "r") as fp:
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


def longest_common_substring(seqs):
    return ""


seqs = read_input()
