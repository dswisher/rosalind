
import unittest
from . import main


class TestLongestSubsequence(unittest.TestCase):

    def test_sample1(self):
        n = 5
        pi = [5, 1, 4, 2, 3]
        ei = [1, 2, 3]
        ed = [5, 4, 2]
        ai = main.longest_increasing_subsequence(n, pi)
        ad = main.longest_decreasing_subsequence(n, pi)
        self.assertItemsEqual(ai, ei)
        self.assertItemsEqual(ad, ed)


if __name__ == '__main__':
    unittest.main()
