import sys

if len(sys.argv) < 2:
    print "Usage: python main.py file"
    sys.exit(1)

fname = sys.argv[1]

with open(fname, "r") as fp:
    num = 0
    for line in fp:
        num += 1
        if (num % 2) == 0:
            print line.strip()
