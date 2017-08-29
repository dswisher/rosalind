
import sys


def num_subsets(n):
    # Compute piecemeal, to avoid overflow.
    prod = 1
    for i in xrange(0, n):
        prod = (prod * 2) % 1000000
    return prod


def main():
    if len(sys.argv) != 2:
        print "You must enter n!"
        sys.exit(1)

    n = int(sys.argv[1])

    print num_subsets(n)


main()
