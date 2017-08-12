import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)

fname = sys.argv[1]
f = open(fname, 'r')
dna = f.read()
f.close()
num = {}

for c in dna:
    if c in num:
        num[c] += 1
    else:
        num[c] = 1

print '{} {} {} {}'.format(num["A"], num["C"], num["G"], num["T"])
