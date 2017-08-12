import sys

if len(sys.argv) < 3:
    print 'Usage: fib.py n k'
    sys.exit(1)

n = int(sys.argv[1])
k = int(sys.argv[2])

# Recurrance: F(i) = F(i-1) + k*F(i-2)
pop = [1, 1]
for i in range(2, n):
    p = pop[i-1] + k * pop[i-2]
    pop.append(p)

print pop[n-1]
