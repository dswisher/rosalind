
import unittest
from . import main
from rosalind.bioinformatics.common import seqio


class TestCircularChromosomeAssembly(unittest.TestCase):

    def test_sample1(self):
        seqs = seqio.read_list("sample1.txt", __file__)
        expected = "GATTACA"
        self.run_test(seqs, expected)

    def test_sample2(self):
        seqs = seqio.read_list("sample2.txt", __file__)
        expected = seqio.read_one("expected2.txt", __file__)
        self.run_test(seqs, expected)

    def run_test(self, seqs, expected):
        actual = main.assemble_circular_chromosome(seqs)
        # The cycle can start anywhere, so double up and look for substring
        self.assertEquals(len(actual), len(expected))
        self.assertTrue((expected + expected).find(actual) != -1)


if __name__ == '__main__':
    unittest.main()
