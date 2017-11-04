
import sys

if len(sys.argv) < 2:
    print("Usage: python main.py file")
    sys.exit(1)

fname = sys.argv[1]

with open(fname, "r") as fp:
    s = fp.readline().strip()
    a, b, c, d = map(int, fp.readline().split())

s1 = s[a:b+1]
s2 = s[c:d+1]

print(s1, s2)
