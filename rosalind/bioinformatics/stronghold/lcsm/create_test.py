
import sys
import string
import random


# https://stackoverflow.com/a/2030081/282725
def random_string(l):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(l))


def insert_at_random(big, little):
    pos = random.randint(0, len(big))
    return big[:pos] + little + big[pos:]


if len(sys.argv) != 4:
    print "usage: python create_test.py n m substr"
    print "   where n = number of strings to create"
    print "         m = length of each string"
    print "         substr is the string to embed"
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])
substr = sys.argv[3]

print n, m, substr

l = m - len(substr)

if l < 10:
    print "m - len(substr) must be at least 10."
    sys.exit(1)

seqs = []
for i in xrange(n):
    rs = random_string(l)
    print insert_at_random(rs, substr)
