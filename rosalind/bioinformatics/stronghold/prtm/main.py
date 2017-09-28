
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import masses


def calc_mass(prot):
    mass = 0    # Ignore extra water, which would add 18.01056
    for c in prot:
        mass += masses.get_mass(c)
    return mass


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        protein = fp.readline().strip()
    print calc_mass(protein)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
