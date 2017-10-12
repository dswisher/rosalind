
import unittest
from . import main


class TestLongestCommonSubstring(unittest.TestCase):

    def test_sample1(self):
        s1 = "AACCTTGG"
        s2 = "ACACTGTGA"
        actual = main.find_longest_common_subsequence(s1, s2)
        expected = "AACTGG"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
