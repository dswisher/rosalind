import sys

if len(sys.argv) < 3:
    print "Usage: python main.py a b"
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

print a**2 + b**2
