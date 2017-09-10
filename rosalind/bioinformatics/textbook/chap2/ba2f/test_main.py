
import unittest
from . import main


class TestRandomizedMotifSearch(unittest.TestCase):

    @unittest.skip("under construction")
    def test_sample(self):
        k = 8
        t = 5
        dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
               "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
               "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
               "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
               "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
        expected = ["TCTCGGGG", "CCAAGGTG", "TACAGGCG",
                    "TTCAGGTG", "TCCACGTG"]
        motifs = main.randomized_motif_search(dna, k, t)
        self.assertItemsEqual(motifs, expected)


if __name__ == '__main__':
    unittest.main()
