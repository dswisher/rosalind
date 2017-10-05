
import unittest
from . import main
from rosalind.common import util
from rosalind.bioinformatics.common import seqio


class TestRandomMotifs(unittest.TestCase):

    def test_sample1(self):
        dna = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
        protein = "MA"
        expected = ["ATGGCC", "GGCCAT", "ATGGCC"]
        actual = main.find_encodings(dna, protein)
        self.assertItemsEqual(actual, expected)

    def test_sample2(self):
        with open(util.find_file("sample2.txt", __file__), "r") as fp:
            dna = fp.readline().strip()
            protein = fp.readline().strip()
        expected = seqio.read_list("expected2.txt", __file__)
        actual = main.find_encodings(dna, protein)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
