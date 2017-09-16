
from __future__ import print_function
import sys
import time
from rosalind.common import util


def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)


def build_overlap_graph(seqs):
    adj_list = []
    # TODO - O(n^2) is SLOW; is there a better way?
    for p in seqs:
        for pp in seqs:
            if p != pp and p[1:] == pp[:-1]:
                adj_list.append((p, pp))
    return adj_list


def main(fname):
    start = time.time()
    seqs = []
    with open(util.find_file(sys.argv[1]), "r") as fp:
        for line in fp:
            seqs.append(line.strip())
    result = build_overlap_graph(seqs)
    for p in result:
        print (p[0], "->", p[1])
    end = time.time()
    eprint(round((end - start), 5))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
