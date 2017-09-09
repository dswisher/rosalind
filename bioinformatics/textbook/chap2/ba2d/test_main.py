
import unittest
from . import main


class TestGreedyMotifSearch(unittest.TestCase):

    def test_sample(self):
        k = 3
        t = 5
        dna = ["GGCGTTCAGGCA",
               "AAGAATCAGTCA",
               "CAAGGAGTTCGC",
               "CACGTCAATCAC",
               "CAATAATATTCG"]
        expected = ["CAG", "CAG", "CAA", "CAA", "CAA"]
        motifs = main.greedy_motif_search(dna, k, t)
        self.assertItemsEqual(motifs, expected)


if __name__ == '__main__':
    unittest.main()
