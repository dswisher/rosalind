
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import masses


def infer_peptide(parent, weights):
    # Lump together pairs of weights that sum to the parent mass
    matches = {}
    for i in xrange(len(weights)):
        for j in xrange(i, len(weights)):
            diff = weights[j] - weights[i]
            closest = masses.get_amino_acid(diff)
            if closest:
                tup = (closest, weights[j])
                if weights[i] in matches:
                    matches[weights[i]].append(tup)
                else:
                    matches[weights[i]] = [tup]

    # Build up the protein by adding the next smallest item
    tot = min(matches)
    protein = ''
    n = (len(weights) - 2) / 2      # 2n + 2 masses in list
    while len(protein) < n:
        entry = matches[tot][0]     # TODO - backtrack to other items?
        protein += entry[0]
        tot = entry[1]

    return protein


def main(fname):
    L = []
    with open(util.find_file(fname), "r") as fp:
        for line in fp:
            L.append(float(line))
    print infer_peptide(L[0], L[1:])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
