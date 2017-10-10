
import unittest
from . import main


class TestRandomMotifs(unittest.TestCase):

    def test_sample1(self):
        n = 6
        m = 3
        num = main.count_subsets(n, m)
        self.assertEquals(num, 42)

    def test_sample2(self):
        n = 1990
        m = 908
        num = main.count_subsets(n, m)
        self.assertEquals(num, 375952)


if __name__ == '__main__':
    unittest.main()
