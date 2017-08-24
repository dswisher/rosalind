
import sys

if len(sys.argv) != 2:
    print "You must enter the name of the file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    num = int(file.readline())
    edges = 0
    while file.readline():
        edges += 1

print num - edges - 1

