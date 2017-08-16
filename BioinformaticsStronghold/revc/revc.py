import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)

comp = { 'A':'T', 'C':'G', 'G':'C', 'T':'A'}
s = file(sys.argv[1]).read()
sc = ''
for c in reversed(s):
    if c in comp:
        sc += comp[c]

print sc

