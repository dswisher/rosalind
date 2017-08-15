
import sys

if len(sys.argv) != 2:
    print "You must specify the name of the file to load."
    sys.exit(1)

def read_prot(fname):
    with open(fname, "r") as file:
        return file.readline().strip()

def get_mass(aa):
    return { "A":  71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841, "G":  57.02146,
             "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
             "P":  97.05276, "Q": 128.05858, "R": 156.10111, "S":  87.03203, "T": 101.04768, "V":  99.06841,
             "W": 186.07931, "Y": 163.06333 }[aa]

def calc_mass(prot):
    mass = 0    # Ignore extra water, which would add 18.01056
    for c in prot:
        mass += get_mass(c)
    return mass

print calc_mass(read_prot(sys.argv[1]))

