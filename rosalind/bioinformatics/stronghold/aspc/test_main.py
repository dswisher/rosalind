
import unittest
from . import main


class TestRandomMotifs(unittest.TestCase):

    def test_sample1(self):
        n = 6
        m = 3
        num = main.count_subsets(n, m)
        self.assertEquals(num, 42)

    def test_sample2(self):
        # TODO - submitted answer failed; come up with additional test case
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
