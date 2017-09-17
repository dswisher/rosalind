
import unittest
from . import main


class TestShortestSuperstring(unittest.TestCase):

    def test_max_overlap(self):
        self.assertEquals()

    def test_sample1(self):
        seqs = ["ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC"]
        sup = main.find_shortest_superstring(seqs)
        self.assertEquals(sup, "ATTAGACCTGCCGGAATAC")


if __name__ == '__main__':
    unittest.main()
