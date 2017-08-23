
import sys
import math

if len(sys.argv) != 2:
    print "Please enter the name of the file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    seq = file.readline().strip()
    gcContent = map(float, file.readline().split())

result = []
for x in gcContent:
    aaProbs = {
            'G': x / 2.0,
            'C': x / 2.0,
            'A': (1 - x) / 2.0,
            'T': (1 - x) / 2.0
            }

    cProb = 0
    for c in seq:
        cProb += math.log10(aaProbs[c])

    result.append(round(cProb, 5))

print " ".join(map(str, result))

