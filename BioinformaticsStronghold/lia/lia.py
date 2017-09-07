
import sys

if len(sys.argv) != 3:
    print "Usage: k N"
    sys.exit(1)

k = int(sys.argv[1])
N = int(sys.argv[2])


def fact(x):
    if x <= 1:
        return 1
    return x * fact(x-1)


def binomial(n, k):
    return float(fact(n)) / (fact(k) * fact(n-k))


def bernoulli_trial(n, p, k):
    return binomial(n, k) * pow(p, k) * pow(1-p, n-k)


sum = 0
tot = pow(2, k)
for i in xrange(N, 1 + tot):
    sum += bernoulli_trial(tot, 0.25, i)

print sum
