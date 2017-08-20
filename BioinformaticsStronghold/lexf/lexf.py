
import sys

if len(sys.argv) != 2:
    print "You must enter the name of the file to open!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    symbols = sorted(file.readline().strip().split())
    n = int(file.readline())

def enumerate(symbols, n, prefix):
    if len(prefix) == n:
        print prefix
    else:
        for c in symbols:
            enumerate(symbols, n, prefix + c)


enumerate(symbols, n, "")

