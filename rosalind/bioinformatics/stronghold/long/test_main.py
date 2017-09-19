
import unittest
from . import main


class TestShortestSuperstring(unittest.TestCase):

    def test_max_overlap(self):
        self.assertEquals(main.max_overlap("AABB", "CCDD"), 0)
        self.assertEquals(main.max_overlap("AABC", "CCDD"), 1)
        self.assertEquals(main.max_overlap("AACC", "CCDD"), 2)
        self.assertEquals(main.max_overlap("AABC", "BCDD"), 2)

    def test_sample1(self):
        seqs = ["ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC"]
        sup = main.find_shortest_superstring(seqs)
        self.assertEquals(sup, "ATTAGACCTGCCGGAATAC")


if __name__ == '__main__':
    unittest.main()
