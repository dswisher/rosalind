
import sys
import os
from ....common import kmers


def read_data(fname):
    dna = []
    with open(fname, "r") as fp:
        k, t = map(int, fp.readline().split())
        for line in fp:
            dna.append(line.strip())
    return (k, t, dna)


# Build a list of lists of k-mers (one per string in dna)
def build_kmers(dna, k):
    klist = []
    for s in dna:
        l = []
        klist.append(l)
        for mer in kmers.enumerate(s, k):
            l.append(mer)
    return klist


def randomized_motif_search(dna, k, t):
    all_kmers = build_kmers(dna, k)
    best_motifs = [item[0] for item in all_kmers]
    best_score = sys.maxint
    for kmer in all_kmers[0]:
        motifs = [kmer]
        for i in xrange(1, t):
            seed = 1.0 / len(motifs)
            profile = kmers.build_profile(motifs, k, seed)
            motif_i = kmers.find_most_probable(profile, dna[i], k)
            motifs.append(motif_i)
        profile = kmers.build_profile(motifs, k, seed)
        consensus = kmers.find_consensus(profile, k)
        score = kmers.compute_score(consensus, motifs)
        if score < best_score:
            best_score = score
            best_motifs = motifs
    return best_motifs


def main(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    k, t, dna = read_data(path)
    motifs = randomized_motif_search(dna, k, t)
    for m in motifs:
        print m

    # test1()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
