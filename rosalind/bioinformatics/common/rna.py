
trans = {
            "UUU": "F",    "CUU": "L",  "AUU": "I",  "GUU": "V",
            "UUC": "F",    "CUC": "L",  "AUC": "I",  "GUC": "V",
            "UUA": "L",    "CUA": "L",  "AUA": "I",  "GUA": "V",
            "UUG": "L",    "CUG": "L",  "AUG": "M",  "GUG": "V",
            "UCU": "S",    "CCU": "P",  "ACU": "T",  "GCU": "A",
            "UCC": "S",    "CCC": "P",  "ACC": "T",  "GCC": "A",
            "UCA": "S",    "CCA": "P",  "ACA": "T",  "GCA": "A",
            "UCG": "S",    "CCG": "P",  "ACG": "T",  "GCG": "A",
            "UAU": "Y",    "CAU": "H",  "AAU": "N",  "GAU": "D",
            "UAC": "Y",    "CAC": "H",  "AAC": "N",  "GAC": "D",
            "UAA": "STOP", "CAA": "Q",  "AAA": "K",  "GAA": "E",
            "UAG": "STOP", "CAG": "Q",  "AAG": "K",  "GAG": "E",
            "UGU": "C",    "CGU": "R",  "AGU": "S",  "GGU": "G",
            "UGC": "C",    "CGC": "R",  "AGC": "S",  "GGC": "G",
            "UGA": "STOP", "CGA": "R",  "AGA": "R",  "GGA": "G",
            "UGG": "W",    "CGG": "R",  "AGG": "R",  "GGG": "G"
        }


def translate(seq):
    prot = ""
    codon = ""
    for n in seq:
        codon += n
        if len(codon) == 3:
            if codon in trans:
                if trans[codon] == "STOP":
                    break
                prot += trans[codon]
            else:
                # TODO - better way to handle unknown codon?
                prot += "X"
            codon = ""
    return prot