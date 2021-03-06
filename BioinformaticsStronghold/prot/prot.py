import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)

# Populate the codon map
trans = {
            "UUU": "F",  "CUU": "L",  "AUU": "I",  "GUU": "V",
            "UUC": "F",  "CUC": "L",  "AUC": "I",  "GUC": "V",
            "UUA": "L",  "CUA": "L",  "AUA": "I",  "GUA": "V",
            "UUG": "L",  "CUG": "L",  "AUG": "M",  "GUG": "V",
            "UCU": "S",  "CCU": "P",  "ACU": "T",  "GCU": "A",
            "UCC": "S",  "CCC": "P",  "ACC": "T",  "GCC": "A",
            "UCA": "S",  "CCA": "P",  "ACA": "T",  "GCA": "A",
            "UCG": "S",  "CCG": "P",  "ACG": "T",  "GCG": "A",
            "UAU": "Y",  "CAU": "H",  "AAU": "N",  "GAU": "D",
            "UAC": "Y",  "CAC": "H",  "AAC": "N",  "GAC": "D",
            "UAA": "",   "CAA": "Q",  "AAA": "K",  "GAA": "E",
            "UAG": "",   "CAG": "Q",  "AAG": "K",  "GAG": "E",
            "UGU": "C",  "CGU": "R",  "AGU": "S",  "GGU": "G",
            "UGC": "C",  "CGC": "R",  "AGC": "S",  "GGC": "G",
            "UGA": "",   "CGA": "R",  "AGA": "R",  "GGA": "G",
            "UGG": "W",  "CGG": "R",  "AGG": "R",  "GGG": "G"
        }

# Load the file and do the translation
s = file(sys.argv[1]).read()
prot = ''
codon = ''
for c in s:
    codon += c
    if len(codon) == 3:
        if codon in trans:
            prot += trans[codon]
        else:
            prot += "X"
        codon = ''

# Results!
print prot

