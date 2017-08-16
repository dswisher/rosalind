import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)

s = file(sys.argv[1]).read()
rna = ''
for c in s:
    if c == 'T':
        rna += 'U'
    else:
        rna += c

print rna

