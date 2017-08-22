
import sys

if len(sys.argv) != 2:
    print "You must enter the name of a file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    index = int(file.readline())
    k = int(file.readline())

def number_to_symbol(i):
    return { 0: 'A', 1: 'C', 2:'G', 3:'T' }[i]

def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefixIndex = index / 4
    r = index % 4
    symbol = number_to_symbol(r)
    prefixPattern = number_to_pattern(prefixIndex, k - 1)
    return prefixPattern + symbol

print number_to_pattern(index, k)


