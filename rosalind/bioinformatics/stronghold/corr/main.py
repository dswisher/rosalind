
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import fasta
from rosalind.bioinformatics.common import kmers


def build_sets(seqs):
    good = set()
    bad = set()
    for s in seqs:
        if seqs.count(s) > 1:
            good.add(s)
        elif kmers.reverse_complement(s) in seqs:
            good.add(s)
        else:
            bad.add(s)
    return (good, bad)


def find_corrections(seqs):
    corr = []
    good_reads, bad_reads = build_sets(seqs)
    for s1 in bad_reads:
        for s2 in good_reads:
            if kmers.hamming_distance(s1, s2) == 1:
                corr.append(s1 + "->" + s2)
                break
            else:
                c2 = kmers.reverse_complement(s2)
                if kmers.hamming_distance(s1, c2) == 1:
                    corr.append(s1 + "->" + c2)
                    break
    # print good_reads
    # print bad_reads
    return corr


def main(fname):
    seqs, _ = fasta.read(util.find_file(fname))
    corrections = find_corrections(seqs)
    for c in corrections:
        print c


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("You must specify the name of the data file to load!")
        sys.exit(1)
    main(sys.argv[1])
