
import sys

if len(sys.argv) != 2:
    print "Enter the number of leaf nodes."
    sys.exit(1)

n = int(sys.argv[1])

print n - 2
