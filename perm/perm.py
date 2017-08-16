
import sys

if len(sys.argv) < 2:
    print "You must specify n"
    sys.exit(1)

n = int(sys.argv[1])

def fact(x):
    if x <= 1: return 1
    return x * fact(x-1)

def permute(items, prefix):
    if len(items) > 0:
        for i in xrange(len(items)):
            permute(items[:i] + items[i+1:], prefix + [items[i]])
    else:
        print " ".join(map(str,prefix))

print fact(n)
permute(range(1, n + 1), [])

