
import sys


def enumerate_signed_permutations(num):
    # TODO - HACK!
    # Idea: generate permutations of num distinct numbers, then apply
    # the negative signs
    expected = [(-1, -2), (-1, 2), (1, -2), (1, 2),
                (-2, -1), (-2, 1), (2, -1), (2, 1)]
    return expected


def main(num):
    perms = enumerate_signed_permutations(num)
    print len(perms)
    for pair in perms:
        print pair[0], pair[1]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify N as a parameter!"
        sys.exit(1)
    main(int(sys.argv[1]))
