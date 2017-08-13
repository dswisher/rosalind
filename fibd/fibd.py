import sys

if len(sys.argv) < 3:
    print 'Usage: fib.py n m'
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

age = [0] * m
age[0] = 1

for i in range(1, n):
    born = sum(age[1:m])

    for j in range(m - 1, 0, -1):
        age[j] = age[j-1]

    age[0] = born

print sum(age)

