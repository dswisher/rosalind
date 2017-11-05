import sys

if len(sys.argv) < 3:
    print "Usage: python main.py a b"
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

sum = 0
for i in xrange(a, b + 1):
    if (i % 2) == 1:
        sum += i

print sum
