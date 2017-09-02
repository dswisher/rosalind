
import sys
from biotools import enumerate_kmers

if len(sys.argv) != 2:
    print "Please enter the name of the data file."
    sys.exit(1)

with open(sys.argv[1], "r") as fp:
    k = int(fp.readline())
    seq = fp.readline().strip()

for kmer in sorted(enumerate_kmers(seq, k)):
    print kmer
