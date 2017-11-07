import sys

if len(sys.argv) < 2:
    print "Usage: python main.py file"
    sys.exit(1)

word_counts = dict()
fname = sys.argv[1]

with open(fname, "r") as fp:
    for line in fp:
        bits = line.strip().split()
        for word in bits:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

for key in sorted(word_counts):
    print key, word_counts[key]
