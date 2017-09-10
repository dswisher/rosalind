
import unittest
from . import kmers


class TestKMers(unittest.TestCase):

    k = 12
    expected = [[0.20, 0.20, 0.00, 0.00, 0.00, 0.00, 0.90, 0.10, 0.10, 0.10, 0.30, 0.00],   # noqa
                [0.10, 0.60, 0.00, 0.00, 0.00, 0.00, 0.00, 0.40, 0.10, 0.20, 0.40, 0.60],   # noqa
                [0.00, 0.00, 1.00, 1.00, 0.90, 0.90, 0.10, 0.00, 0.00, 0.00, 0.00, 0.00],   # noqa
                [0.70, 0.20, 0.00, 0.00, 0.10, 0.10, 0.00, 0.50, 0.80, 0.70, 0.30, 0.40]]   # noqa

    def test_profile(self):
        actual = kmers.build_profile(["TCGGGGGTTTTT", "CCGGTGACTTAC",
                                      "ACGGGGATTTTC", "TTGGGGACTTTT",
                                      "AAGGGGACTTCC", "TTGGGGACTTCC",
                                      "TCGGGGATTCAT", "TCGGGGATTCCT",
                                      "TAGGGGAACTAC", "TCGGGTATAACC"], self.k)
        for i in xrange(len(self.expected)):
            for j in xrange(self.k):
                self.assertAlmostEqual(actual[i][j], self.expected[i][j])

    def test_find_consensus(self):
        actual = kmers.find_consensus(self.expected, self.k)
        self.assertEqual(actual, "TCGGGGATTTCC")


if __name__ == '__main__':
    unittest.main()
