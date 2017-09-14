
import itertools
import sys


def apply_bitmask(nums, m):
    items = list(nums)
    for i in xrange(len(items) + 1):
        if m & 1:
            items[i] = -items[i]
        m = m >> 1
    return tuple(items)


def enumerate_signed_permutations(num):
    perms = []
    numbers = [i+1 for i in xrange(num)]
    for p in itertools.permutations(numbers):
        for m in xrange(2 ** num):
            perms.append(apply_bitmask(p, m))
    return perms


def main(num):
    perms = enumerate_signed_permutations(num)
    print len(perms)
    for item in perms:
        print " ".join(map(str, item))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify N as a parameter!"
        sys.exit(1)
    main(int(sys.argv[1]))
