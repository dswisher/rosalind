
import unittest
from rosalind.common import util
from . import main


class TestGreedyMotifSearchWithPseudoCounts(unittest.TestCase):

    def test_sample1(self):
        k = 3
        d = 1
        dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
        expected = ["ATA", "ATT", "GTT", "TTT"]
        motifs = main.motif_enumeration(dna, k, d)
        self.assertItemsEqual(motifs, expected)

    # TODO - too slow
    # def test_sample2(self):
    #     k = 5
    #     d = 2
    #     dna = [
    #             "TCTGAGCTTGCGTTATTTTTAGACC",
    #             "GTTTGACGGGAACCCGACGCCTATA",
    #             "TTTTAGATTTCCTCAGTCCACTATA",
    #             "CTTACAATTTCGTTATTTATCTAAT",
    #             "CAGTAGGAATAGCCACTTTGTTGTA",
    #             "AAATCCATTAAGGAAAGACGACCGT"
    #             ]
    #     expected = self.read_expected("expected2.txt")
    #     motifs = main.motif_enumeration(dna, k, d)
    #     self.assertItemsEqual(motifs, expected)

    def read_expected(self, fname):
        with open(util.find_file(fname, __file__), "r") as fp:
            seqs = fp.readline().split()
        return seqs


if __name__ == '__main__':
    unittest.main()
