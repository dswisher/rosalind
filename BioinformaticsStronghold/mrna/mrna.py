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
prot = file(sys.argv[1]).read().strip()
count = 3   # Three stop codons in every protein
for aa in prot:
    num = trans.values().count(aa)
    count = (count * num) % 1000000

# Results!
print count

