
import sys
import random
from rosalind.common import util
from rosalind.bioinformatics.common import kmers


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


def do_one_search(dna, k, t):
    all_kmers = build_kmers(dna, k)
    # best_motifs = [item[0] for item in all_kmers]
    motifs = [item[random.randint(0, len(item) - 1)] for item in all_kmers]
    best_motifs = motifs
    best_score = sys.maxint
    seed = 1.0 / len(motifs)

    while True:
        # Construct a profile from the motifs we have so far
        profile = kmers.build_profile(motifs, k, seed)

        # Find the profile-most-probable k-mers from each DNA string
        motifs = []
        for i in xrange(0, t):
            motifs.append(kmers.find_most_probable(profile, dna[i], k))

        # Compute the score of this new set of motifs
        profile = kmers.build_profile(motifs, k, seed)
        consensus = kmers.find_consensus(profile, k)
        score = kmers.compute_score(consensus, motifs)

        if score < best_score:
            best_score = score
            best_motifs = motifs
        else:
            return (best_score, best_motifs)


def randomized_motif_search(dna, k, t):
    best_score = sys.maxint
    best_motifs = None
    for i in xrange(0, 1000):
        if i % 10 == 0:
            print "Iter", i
        score, motifs = do_one_search(dna, k, t)
        if score < best_score:
            print " -> improved score:", score, "<", best_score
            best_score = score
            best_motifs = motifs
    print "Final best_score:", best_score
    return best_motifs


def main(fname):
    k, t, dna = read_data(util.find_file(fname))
    motifs = randomized_motif_search(dna, k, t)
    for m in motifs:
        print m

    # test1()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
