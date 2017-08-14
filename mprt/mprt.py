import os.path
import regex
import requests
import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)

def load_names(fname):
    with open(fname, "r") as file:
        return [line.rstrip('\n') for line in file]

def download_fasta(name):
    fname = name + ".fasta"
    if not os.path.isfile(fname):
        print "File " + fname + " not found - downloading..."
        url = "http://www.uniprot.org/uniprot/" + fname
        r = requests.get(url)
        with open(fname, "w") as file:
            file.write(r.content)
    return fname

def read_fasta(fname):
    seq = ""
    with open(fname, "r") as file:
        for line in file:
            line = line.strip()
            if line[0] != '>':
                seq += line
    return seq

def find_motifs(seq, pattern):
    pos = []
    # Using the regex package, as the stock regex library does not handle overlaps
    for match in regex.finditer(pattern, seq, overlapped=True):
        pos.append(match.start() + 1)
    return pos

names = load_names(sys.argv[1])
for name in names:
    fname = download_fasta(name)
    seq = read_fasta(fname)
    locs = find_motifs(seq, "N[A-OQ-Z][ST][A-OQ-Z]")
    if len(locs) > 0:
        print name
        print " ".join(map(str, locs))

