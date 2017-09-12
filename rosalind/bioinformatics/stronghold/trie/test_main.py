
import unittest
from . import main


class TestTrie(unittest.TestCase):

    def test_sample(self):
        dna = ["ATAGA", "ATC", "GAT"]
        expected = [[1, 2, 'A'], [2, 3, 'T'], [3, 4, 'A'],
                    [4, 5, 'G'], [5, 6, 'A'], [3, 7, 'C'],
                    [1, 8, 'G'], [8, 9, 'A'], [9, 10, 'T']]
        actual = main.get_adjacency(main.make_trie(dna))
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
