
import unittest
from . import main


class TestShortestSuperstring(unittest.TestCase):

    def test_sample1(self):
        seq = "AGCUAGUCAU"
        num = main.calc_matches(seq)
        self.assertEquals(num, 12)

    def test_sample2(self):
        seq = "AUUCGGAUAAAAGACCUUUUACGAAAUGACCGAGGGGUACUCCGCGAUCCGCUGCGCAAUCACCUGUAGGUGACUGUCUU"    # noqa
        num = main.calc_matches(seq)
        self.assertEquals(num, 5919012181389927685417441689600000000)


if __name__ == '__main__':
    unittest.main()
