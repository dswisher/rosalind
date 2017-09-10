
import unittest
from . import main


class TestGreedyMotifSearchWithPseudoCounts(unittest.TestCase):

    def test_sample(self):
        k = 3
        t = 5
        dna = ["GGCGTTCAGGCA",
               "AAGAATCAGTCA",
               "CAAGGAGTTCGC",
               "CACGTCAATCAC",
               "CAATAATATTCG"]
        expected = ["TTC", "ATC", "TTC", "ATC", "TTC"]
        motifs = main.greedy_motif_search(dna, k, t)
        self.assertItemsEqual(motifs, expected)


if __name__ == '__main__':
    unittest.main()
