
import unittest
from . import main
from rosalind.bioinformatics.common import debruijn


class TestConstructDebruijn(unittest.TestCase):

    def test_sample1(self):
        seqs = ["TGAT", "CATG", "TCAT", "ATGC", "CATC", "CATC"]
        graph = main.make_graph(seqs)
        actual = list(debruijn.format_adjacency(graph))
        expected = ["(ATC, TCA)", "(ATG, TGA)", "(ATG, TGC)",
                    "(CAT, ATC)", "(CAT, ATG)", "(GAT, ATG)",
                    "(GCA, CAT)", "(TCA, CAT)", "(TGA, GAT)"]
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
