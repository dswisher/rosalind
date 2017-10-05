
import sys
import re
from rosalind.common import util
from rosalind.bioinformatics.common import rna
from rosalind.bioinformatics.common import kmers


def build_regex(protein):
    expr = ""
    for aa in protein:
        seg = "("
        for codon in rna.reverse_translate(aa):
            if len(seg) > 1:
                seg += "|"
            seg += codon.replace("U", "T")
        seg += ")"

        expr += seg
    return expr


def find_encodings(dna, protein):
    encodings = []
    expr = build_regex(protein)

    for m in re.finditer(expr, dna):
        encodings.append(m.group(0))

    for m in re.finditer(expr, kmers.reverse_complement(dna)):
        encodings.append(kmers.reverse_complement(m.group(0)))

    return encodings


def main(fname):
    with open(util.find_file(fname), "r") as fp:
        dna = fp.readline().strip()
        protein = fp.readline().strip()
    for e in find_encodings(dna, protein):
        print e


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
