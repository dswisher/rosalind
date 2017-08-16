import sys

if len(sys.argv) < 2:
    print 'You must specify the name of the file to load.'
    sys.exit(1)


def read_fasta(fname):
    seq = ""
    with open(fname, "r") as file:
        for line in file:
            line = line.strip()
            if line[0] != '>':
                seq += line
    return seq


def transcribe(seq):
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


def find_prot(seq):
    found = set()
    for i in xrange(len(seq) - 2):
        if seq[i] == 'A' and seq[i+1] == 'T' and seq[i+2] == 'G':
            prot = transcribe(seq[i:])
            if len(prot) > 0:
                found.add(prot)
    return found


def rev_comp(seq):
    comp = { 'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    seq = file(sys.argv[1]).read()
    sc = ''
    for c in reversed(seq):
        if c in comp:
            sc += comp[c]
    return sc


def main():
    seq = read_fasta(sys.argv[1])
    for s in find_prot(seq) | find_prot(rev_comp(seq)):
        print s


main()

