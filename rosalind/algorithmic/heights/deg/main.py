
import sys
from rosalind.common import util

if len(sys.argv) != 2:
    print "Please enter the name of the data file to load!"
    sys.exit(1)

nums = []
with open(util.find_file(sys.argv[1]), "r") as fp:
    n, m = map(int, fp.readline().split())
    for line in fp.readlines():
        a, b = map(int, line.split())
        nums.append(a)
        nums.append(b)

deg = [0] * n

for i in xrange(len(nums)):
    deg[nums[i] - 1] += 1

print " ".join(map(str, deg))
