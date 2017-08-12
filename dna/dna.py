import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)

s = file(sys.argv[1]).read()
print s.count("A"), s.count("G"), s.count("C"), s.count("T")

