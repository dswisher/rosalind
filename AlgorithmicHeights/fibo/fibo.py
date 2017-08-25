
import sys
import time

if len(sys.argv) != 2:
    print "Usage: python fibo.py N"
    sys.exit(1)

n = int(sys.argv[1])

def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    f0 = 0
    f1 = 1
    for x in xrange(n-1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f1

start_time = time.time()
print "fib1:", fib1(n)
elapsed_time = time.time() - start_time
print "Elapsed time:", round(elapsed_time, 5)

print ""

start_time = time.time()
print "fib2:", fib2(n)
elapsed_time = time.time() - start_time
print "Elapsed time:", round(elapsed_time, 5)

