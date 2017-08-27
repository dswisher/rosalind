
import sys
from biotools import neighbors, hamming_distance


def read_data():
    if len(sys.argv) != 2:
        print "You must enter the name of the file to load!"
        sys.exit(1)

    seqs = []
    lineno = 0
    with open(sys.argv[1]) as fp:
        for line in fp:
            lineno += 1
            if lineno == 1:
                k, d = map(int, line.split())
            else:
                seq = line.strip()
                seqs.append(seq)

    return (k, d, seqs)


def list_kmers(dna, k):
    seen = set()
    for seq in dna:
        for i in xrange(0, 1 + len(seq) - k):
            subj = seq[i:i+k]
            if subj not in seen:
                seen.add(subj)
                yield subj


def fuzzy_contains_kmer(seq, kmer, d):
    k = len(kmer)
    for i in xrange(0, 1 + len(seq) - k):
        subj = seq[i:i+k]
        if hamming_distance(kmer, subj) <= d:
            return True
    return False


def motif_enumeration(dna, k, d):
    patterns = set()
    for pattern in list_kmers(dna, k):
        neighborhood = neighbors(pattern, d)
        for pattern_prime in neighborhood:
            if all(fuzzy_contains_kmer(seq, pattern_prime, d) for seq in dna):
                patterns.add(pattern_prime)
    return patterns


def main():
    k, d, dna = read_data()

    motifs = motif_enumeration(dna, k, d)
    print " ".join(sorted(motifs))


if __name__ == "__main__":
    main()
