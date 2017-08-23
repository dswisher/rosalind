
import sys

if len(sys.argv) != 2:
    print "Please enter the name of the file to read!"
    sys.exit(1)


def read_fasta(fname):
    seqs = []
    with open(fname, "r") as ins:
        for line in ins:
            line = line.strip()
            if line[0] == '>':
                seqs.append('')
            else:
                seqs[len(seqs) - 1] += line
    return seqs


def translate(seq):
    trans = {
            "TTT": "F",  "CTT": "L",  "ATT": "I",  "GTT": "V",
            "TTC": "F",  "CTC": "L",  "ATC": "I",  "GTC": "V",
            "TTA": "L",  "CTA": "L",  "ATA": "I",  "GTA": "V",
            "TTG": "L",  "CTG": "L",  "ATG": "M",  "GTG": "V",
            "TCT": "S",  "CCT": "P",  "ACT": "T",  "GCT": "A",
            "TCC": "S",  "CCC": "P",  "ACC": "T",  "GCC": "A",
            "TCA": "S",  "CCA": "P",  "ACA": "T",  "GCA": "A",
            "TCG": "S",  "CCG": "P",  "ACG": "T",  "GCG": "A",
            "TAT": "Y",  "CAT": "H",  "AAT": "N",  "GAT": "D",
            "TAC": "Y",  "CAC": "H",  "AAC": "N",  "GAC": "D",
            "TAA": "",   "CAA": "Q",  "AAA": "K",  "GAA": "E",
            "TAG": "",   "CAG": "Q",  "AAG": "K",  "GAG": "E",
            "TGT": "C",  "CGT": "R",  "AGT": "S",  "GGT": "G",
            "TGC": "C",  "CGC": "R",  "AGC": "S",  "GGC": "G",
            "TGA": "",   "CGA": "R",  "AGA": "R",  "GGA": "G",
            "TGG": "W",  "CGG": "R",  "AGG": "R",  "GGG": "G"
        }

    prot = ''
    codon = ''
    stopped = False
    for c in seq:
        codon += c
        if len(codon) == 3:
            if codon in trans:
                if trans[codon] == "":
                    stopped = True
                    break
                prot += trans[codon]
            else:
                break
            codon = ''
    if not stopped:
        prot = ''
    return prot


def splice(dna, introns):
    for i in introns:
        start = dna.find(i)
        if start >= 0:
            end = start + len(i)
            dna = dna[:start] + dna[end:]
    return dna


def main(fname):
    seqs = read_fasta(fname)
    spliced = splice(seqs[0], seqs[1:])
    return translate(spliced)


print main(sys.argv[1])

