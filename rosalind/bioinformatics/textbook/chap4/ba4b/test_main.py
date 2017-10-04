
import unittest
from . import main


class TestRandomMotifs(unittest.TestCase):

    def test_sample1(self):
        dna = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
        protein = "MA"
        expected = ["ATGGCC", "GGCCAT", "ATGGCC"]
        actual = main.find_encodings(dna, protein)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
