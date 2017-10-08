
import sys
from rosalind.bioinformatics.common import seqio
from rosalind.bioinformatics.common import masses


def get_all_substrings(string):
    # from https://stackoverflow.com/a/22470158/282725
    length = len(string)
    for i in xrange(length):
        for j in xrange(i + 1, length + 1):
            yield(string[i:j])


def generate_spectrum(protein):
    seen = set()
    m = [0, int(masses.get_protein_mass(protein))]
    for s in get_all_substrings(protein + protein[:(len(protein)/2)+1]):
        if len(s) < len(protein) and s not in seen:
            m.append(int(masses.get_protein_mass(s)))
            seen.add(s)
    return sorted(m)


def main(fname):
    protein = seqio.read_one(fname)
    spec = generate_spectrum(protein)
    print " ".join(map(str, spec))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
