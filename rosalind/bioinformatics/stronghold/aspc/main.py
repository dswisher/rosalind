
import sys
import math


def nCr(n, r):
    # from https://stackoverflow.com/a/4941846/282725
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def count_subsets(n, m):
    num = 0
    for k in xrange(m, n + 1):
        num = (num + nCr(n, k)) % 1000000
    return num


def main(n, m):
    num = count_subsets(n, m)
    print num


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("You must specify n and m!")
        sys.exit(1)
    main(int(sys.argv[1]), int(sys.argv[2]))
