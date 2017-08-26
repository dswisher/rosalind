
import sys

if len(sys.argv) != 2:
    print "You must enter the name of a file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    seq = file.readline().strip()

def symbol_to_number(s):
    return { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }[s]


def pattern_to_number(pat):
    if len(pat) == 0:
        return 0
    symbol = pat[-1:]
    prefix = pat[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


print pattern_to_number(seq)

