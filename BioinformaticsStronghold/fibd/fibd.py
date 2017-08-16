import sys

if len(sys.argv) < 3:
    print 'Usage: fib.py n m'
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

def fib(n,k):
    ages = [1] + [0]*(k-1)
    for i in xrange(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)

print fib(n,m)

