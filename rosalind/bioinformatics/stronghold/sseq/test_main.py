
import unittest
from . import main


class TestFindSubsequence(unittest.TestCase):

    def test_sample(self):
        dna = "ACGTACGTGACG"
        subs = "GTA"
        pos = main.find_subseqs(dna, subs)
        self.assertItemsEqual(pos, [3, 4, 5])

    def test_example(self):
        dna = "TATGCTAAGATC"
        subs = "ACG"
        pos = main.find_subseqs(dna, subs)
        self.assertItemsEqual(pos, [2, 5, 9])


if __name__ == '__main__':
    unittest.main()
