
import unittest
from . import main
from rosalind.bioinformatics.common import seqio


class TestCircularChromosomeAssembly(unittest.TestCase):

    def test_sample1(self):
        seqs = seqio.read_list("sample1.txt", __file__)
        actual = main.assemble_circular_chromosome(seqs)
        expected = "GATTACA"
        # The cycle can start anywhere, so double up and look for substring
        self.assertTrue((expected + expected).find(actual) != -1)


if __name__ == '__main__':
    unittest.main()
