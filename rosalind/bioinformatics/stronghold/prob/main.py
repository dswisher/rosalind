
import sys
import math
from rosalind.common import util


def compute_prob(seq, gcContent):
    result = []
    for x in gcContent:
        aaProbs = {
                'G': x / 2.0,
                'C': x / 2.0,
                'A': (1 - x) / 2.0,
                'T': (1 - x) / 2.0
                }

        cProb = 0
        for c in seq:
            cProb += math.log10(aaProbs[c])

        result.append(round(cProb, 5))
    return result


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        seq = fp.readline().strip()
        gcContent = map(float, fp.readline().split())
    result = compute_prob(seq, gcContent)
    print " ".join(map(str, result))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
